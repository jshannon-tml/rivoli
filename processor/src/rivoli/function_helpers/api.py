""" API function helpers. """
import json
import os
import sys
import typing as t
import urllib.parse as urlparse

import requests
import requests.exceptions

from rivoli import db
from rivoli import protos
from rivoli.function_helpers import exceptions
from rivoli.protobson import bson_format
from rivoli.utils import logging

DRYRUN_POST = os.getenv('API_POST_DRYRUN', 'FALSE') != 'FALSE'

logger = logging.get_logger(__name__)

# These codes allow for an automatic retry.
AUTORETRY_CODES: t.Sequence[t.Union[int, 'protos.ProcessingLog.ErrorCode']] = (
    408, 429, 500, 502, 503, 504,
    protos.ProcessingLog.CONNECTION_ERROR, protos.ProcessingLog.TIMEOUT_ERROR)

# Log requests on errors
# Options might be HTTP_ERROR, UNEXPECTED, ALWAYS, DRYRUN
REQUEST_LOG_CRITERIA = 'ERROR'

# TODO: Create a session and request pooling
# But first figure out if that will leak or cookies
def make_request(method: str, url: str, **kwargs: t.Any) -> t.Any:
  """ Call API, retry, and parse Exceptions. Returns a dict from JSON. """
  timeout = kwargs.pop('timeout', 10)

  apilog = protos.ApiLog(
      id=bson_format.hex_id(),
      dryrun=DRYRUN_POST,
      request=protos.ApiLog.Request(
          method=method.upper(),
          url=url,
          timeout=timeout
      )
  )

  if 'json' in kwargs:
    apilog.request.body = json.dumps(kwargs['json'])

  if method.upper() == 'POST' and DRYRUN_POST:
    logger.warn(f'Skipping API post to {url} because of dryrun')
    return {}

  resp = None

  try:
    resp = requests.request(method, url, timeout=timeout, **kwargs)
    resp.raise_for_status()
  except (requests.exceptions.ConnectionError,
          requests.exceptions.ReadTimeout,
          requests.exceptions.HTTPError) as exc:
    # Various requests exceptions get re-written to Rivoli exceptions with
    # appropriate handling of status codes and determination of auto-retry
    error_code: t.Union[protos.ProcessingLog.ErrorCode, int]

    # By default we raise an ExecutionError, which is a record-level error. In
    # some cases we want to raise a more serious (file-level) error.
    if '[Errno 8] nodename nor servname provided' in str(exc):
      # This is basically a DNS error. It's actually a reraise of a lower-level
      # exception (socket.gaiaerror?) but we'll just parse the string
      raise exceptions.ConfigurationError(
          f'Cannot find host for {urlparse.urlparse(url).netloc}',
          summary='Cannot find host') from exc

    if isinstance(exc, requests.exceptions.HTTPError):
      error_code = exc.response.status_code
    elif isinstance(exc, requests.exceptions.ConnectionError):
      error_code = protos.ProcessingLog.CONNECTION_ERROR
    else: # ReadTimeout
      error_code = protos.ProcessingLog.TIMEOUT_ERROR

    autoretry = error_code in AUTORETRY_CODES

    raise exceptions.ExecutionError(str(exc), auto_retry=autoretry,
        http_response=resp, error_code=error_code)

  else:
    return resp.json()

  finally:
    # Any error, including a non-200, generates an exception. Some will get
    # modified and re-raised as a ConfigurationError or ExecutionError but some
    # Exceptions might come straight through
    exc = sys.exc_info()[1]

    if resp is None:
      # resp will be set in all HTTP responses (including non-200s)
      # It will only be None for exceptions like DNS errors
      apilog.response.exception.type = sys.exc_info()[0].__name__
      apilog.response.exception.message = str(exc)
    else:
      apilog.response.code = resp.status_code
      apilog.response.headers.update(resp.headers)
      apilog.response.elapsed_ms = int(resp.elapsed.microseconds / 1000)
      # Only the first 500k of response text
      apilog.response.content = resp.content.decode()[:500_000]

    # Log all requests
    if True:
      db.get_db().apilog.insert_one(bson_format.from_proto(apilog))

      if exc:
        # Only propagate the ApiLog ID if we actually save the log entry
        setattr(exc, 'api_log_id', apilog.id)


def get(url: str, **kwargs: t.Any) -> t.Any:
  """ Call an API with the GET method. Returns a dict from JSON. """
  return make_request('GET', url, **kwargs)

def post(url: str, data: t.Any, **kwargs: t.Any) -> t.Any:
  """ Posts data as JSON. Returns a dict from JSON. """
  return make_request('POST', url, json=data, **kwargs)