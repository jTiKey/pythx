from typing import Dict, Any
import json
from datetime import datetime
import dateutil.parser
from pythx.core.exceptions import RequestValidationError, RequestDecodeError


ANALYSIS_LIST_KEYS = ("offset", "dateFrom", "dateTo")


class AnalysisListRequest:
    def __init__(self, offset: int, date_from: datetime, date_to: datetime):
        self.offset = offset
        self.date_from = date_from
        self.date_to = date_to

    def validate(self):
        return (self.date_from <= self.date_to) and self.offset >= 0

    @classmethod
    def from_json(cls, json_str: str):
        parsed = json.loads(json_str)
        return cls.from_dict(parsed)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        if not all(k in d for k in ANALYSIS_LIST_KEYS):
            raise RequestDecodeError(
                "Not all required keys {} found in data {}".format(
                    ANALYSIS_LIST_KEYS, d
                )
            )
        req = cls(
            offset=d["offset"],
            date_from=dateutil.parser.parse(d["dateFrom"]),
            date_to=dateutil.parser.parse(d["dateTo"]),
        )
        if not req.validate():
            raise RequestValidationError("Request validation failed for {}".format(req))

        return req

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "offset": self.offset,
            "dateFrom": self.date_from.isoformat(),
            "dateTo": self.date_to.isoformat(),
        }


class AnalysisSubmissionRequest:
    pass


class AnalysisStatusRequest:
    pass


class DetectedIssuesRequest:
    pass
