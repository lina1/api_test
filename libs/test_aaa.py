from libs._jsonschema_format import IFormatChecker

__author__ = 'lina'

import jsonschema
from jsonschema import draft3_format_checker,draft4_format_checker
from jsonschema import validate
from jsonschema import Draft4Validator


# validate(1438932053, {"format": "timestamp"}, format_checker=draft3_format_checker)
#
# instance = {
#     "time": 1438932053
# }

# schema = {
#     # "format": "ip-address"
# }

# validate(123, {"format": "ip-address"}, cls=Draft4Validator)

actual = {
    "time": 22222,
    # "data": [],
    "result": 1
}

expect = {
    "type": "object",
    "properties": {
        "time": {"type": "number"},
        "data": {"type": "array"},
        "result": {"type": "number"}
    }
    # "required": ["time", "data", "result"]
}

if "required" not in expect.keys():


    expect["required"] = []

    for item in expect["properties"].keys():

        expect["required"].append(item)



validate(actual, expect, format_checker=IFormatChecker())



