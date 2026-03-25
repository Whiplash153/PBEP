# JSON Request–Response Case

## Goal
Demonstrate the full JSON request–response cycle in a backend-like flow.

## What was done
Simulated receiving a JSON request as raw text, deserializing it into Python data, applying simple business logic, and serializing the result back into JSON.
Simulated HTTP response headers to show how JSON data is returned to a client.

## Notes
JSON is always handled as text at the transport level and converted to language-specific objects only inside the application.
Business logic exists strictly between deserialization and serialization steps.