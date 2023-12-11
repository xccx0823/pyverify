from functools import wraps
from typing import Optional

from pyverify import Verify
from pyverify.frame.base import Params


def assign(*, query: Optional[dict] = None, form: Optional[dict] = None, json: Optional[dict] = None,
           many: bool = False):
    """Parameter check decorator for flask.

    :param query: Validation rules for query string parameters.
    :param form: Validation rules for form parameters.
    :param json: Validation rules for JSON parameters.
    :param many: Used in conjunction with the defined JSON validation rules.
    """

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            from flask import request  # noqa
            params = Params()

            # json
            if json and request.is_json:
                data = request.get_json(silent=True) or {}
                verified = Verify(data=data, rules=json, many=many)
                params.json = verified.params

            # query
            if query:
                verified = Verify(data=request.args.to_dict(), rules=query)
                params.query = verified.params

            # form
            if form:
                verified = Verify(data=request.form.to_dict(), rules=query)
                params.form = verified.params

            result = func(*args, **kwargs, params=params)
            return result

        return inner

    return wrapper
