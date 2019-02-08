import json
import pytest
import dateutil.parser
from pythx.core.request.models import AnalysisListRequest
from pythx.core.exceptions import RequestDecodeError


OFFSET = 0
DATE_FROM = "2019-02-07T00:40:49.058158"
DATE_TO = "2019-02-08T00:40:49.058158"
VALID_LIST = {"offset": OFFSET, "dateFrom": DATE_FROM, "dateTo": DATE_TO}
VALID_LIST_REQUEST = AnalysisListRequest(
    offset=OFFSET,
    date_from=dateutil.parser.parse(DATE_FROM),
    date_to=dateutil.parser.parse(DATE_TO),
)


def assert_analysis_list_request(req):
    assert req.offset == OFFSET
    assert req.date_from.isoformat() == DATE_FROM
    assert req.date_to.isoformat() == DATE_TO


def test_analysis_list_request_from_valid_json():
    req = AnalysisListRequest.from_json(json.dumps(VALID_LIST))
    assert_analysis_list_request(req)


def test_analysis_list_request_from_invalid_json():
    with pytest.raises(RequestDecodeError):
        AnalysisListRequest.from_json("{}")


def test_analysis_list_request_from_valid_dict():
    req = AnalysisListRequest.from_dict(VALID_LIST)
    assert_analysis_list_request(req)


def test_analysis_list_request_from_invalid_dict():
    with pytest.raises(RequestDecodeError):
        AnalysisListRequest.from_dict({})


def test_analysis_list_request_to_json():
    assert json.loads(VALID_LIST_REQUEST.to_json()) == VALID_LIST


def test_analysis_list_request_to_dict():
    assert VALID_LIST_REQUEST.to_dict() == VALID_LIST
