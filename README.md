# About

Gributils-annotator is an annotation service from streams of
positional messages. It annotates messages with weather data from a
gributils server for the time and place of the message. Messages are
sent and received in newline separated json format over simple tcp
sockets, and the json attribute names used and time format are all
GPSD compatible.

Example input:

    {"lat": 3.14, "lon": 15.92, "timestamp": "1970-01-01T01:02:03.123456Z", "other": "data"}

Output:

    {"lat": 3.14,
     "lon": 15.92,
     "timestamp": "1970-01-01T01:02:03.123456Z",
     "other": "data",
     "grib": [{'parameterName': 'P Pressure',          'parameterUnit': 'Pa',    'value': 101633.03125000001}
              {'parameterName': 'U component of wind', 'parameterUnit': 'm s-1', 'value': -2.898160457611084},
              {'parameterName': 'V component of wind', 'parameterUnit': 'm s-1', 'value': 2.705005645751954}]}

