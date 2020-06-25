# Quote API Technical Takehome

A management system for storing and editing simple quotes.

Requirements were to implement a CRUD REST API for quotes.  See the full [prompt](prompt.md) for details.

Implemented in Python, using the Flask web framework.

Can be run locally or in the provided Dockerfile using `make start` or `make start_docker`.

Future improvements:

- Database to replace temporary runtime storage of quotes and auth
  - Would allow for data persistance, efficent sorting and filtering options by other fields (e.g. return results oldest to newest)
- Addition of unit tests
- GraphQL endpoint instead of multiple rest endpoints/methods, allow for easy exploration of relationships between authors, quotes
- Nginx proxy for SSL support (could also be provided by putting behind cloud hosting load balancer)
