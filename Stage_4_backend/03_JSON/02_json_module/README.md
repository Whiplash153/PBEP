# JSON Serialization and Deserialization

## Goal
Learn how to convert data between Python objects and JSON format using the standard json module.

## What was done
Parsed JSON strings into Python dictionaries using json.loads.
Serialized Python dictionaries back into JSON strings using json.dumps.

## Notes
JSON exists only as a text format, so serialization always produces a string.
Not all Python objects can be serialized to JSON, which may cause runtime errors.