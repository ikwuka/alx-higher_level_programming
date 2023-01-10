#!/usr/bin/python3
""" Module that returns the JSON representation of an object """

import json


def to_json_string(my_obj):
    """
    Return JSON representation of an object.

    Args:
        my_obj: object

    Raises:
        Exception: when the object cannot be encoded.
    """

    return json.dumps(my_obj)
