# hello-world-api

A small, minimal FastAPI-based "Hello World" template API intended as a starting point
for new projects or for demonstrations. It provides a tiny, well-structured folder
layout, a few example routes (health and greetings), and an easily extensible router
structure so you can add features quickly.

This repository is intentionally simple so it can be used to teach patterns for
routing, testing, and local development.

## Features

- FastAPI application with clearly separated router modules
- Example endpoints:
	- `/` - root app welcome message
	- `/api/` - API root
	- `/api/health/` - simple health check
	- `/api/greetings/` - greetings endpoint and personalized greeting
- Uses Pipenv for dependency management (Pipfile included)

## Repository layout

```
Pipfile
README.md
src/
	main.py              # FastAPI app entrypoint
	api/
		api.py             # API router registration
		routes/
			greetings.py     # /api/greetings routes
			health.py        # /api/health route
tests/                 # (empty) add your tests here
```

## Prerequisites

- Python 3.10+ (recommended)
- Pipenv (optional, but the project includes a Pipfile)

If you don't use Pipenv you can create a venv and install FastAPI + Uvicorn directly.

## Quick start (development)

Below are minimal steps to run the API locally using Pipenv. If you prefer virtualenv or other tooling, adapt accordingly.

1. Install pipenv (if you don't have it):

```bash
python -m pip install --user pipenv
```

2. Install dependencies and spawn a shell:

```bash
pipenv install --dev
pipenv shell
```

3. Run the app with Uvicorn from the repository root:

```bash
uvicorn src.main:app --reload --port 8000
```

4. Open your browser or use curl to try the endpoints (examples below).

## API endpoints and examples

Assuming the server runs at http://127.0.0.1:8000:

- App root

	GET /

	Response:
	```json
	{"message": "Hello from the app route!"}
	```

- API root

	GET /api/

	Response:
	```json
	{"message": "Hello from the api route!"}
	```

- Health check

	GET /api/health/

	Response:
	```json
	{"status": "healthy"}
	```

- Greetings

	GET /api/greetings/

	Response:
	```json
	{"message": "Hello from the greetings route!"}
	```

	GET /api/greetings/{name}

	Example: GET /api/greetings/Ian

	Response:
	```json
	{"message": "Hello, Ian!"}
	```

## Interactive docs

FastAPI automatically generates OpenAPI docs. When the app is running you can view:

- Swagger UI: http://127.0.0.1:8000/api/docs
- ReDoc:       http://127.0.0.1:8000/api/redoc

Note: the OpenAPI JSON is mounted at `/api/openapi.json` by the application configuration.

## Testing

This project includes a `tests/` folder with example tests that validate the
basic endpoints. The repository includes one test file:

- `tests/test_endpoints.py` — checks app root, API root, health and greetings
 - `tests/test_main.py` — tests top-level app root (`/`)
 - `tests/api/test_api.py` — tests API router root (`/api/`)
 - `tests/api/routes/test_health.py` — tests `/api/health/`
 - `tests/api/routes/test_greetings.py` — tests `/api/greetings/` and personalized greeting

To run the tests locally, install pytest inside your environment and run:

```bash
pipenv install --dev
pipenv run pytest -q
```

Notes:
- Tests use FastAPI's `TestClient` (Starlette) to exercise the ASGI app directly.
- The test file adjusts `sys.path` to import the `src/main.py` module so it can
	import the `app` object without requiring `src` to be a package. Keep that
	pattern if you add more tests, or convert `src/` into a package by adding
	`src/__init__.py`.

## Development notes

- The main FastAPI instance is defined in `src/main.py`.
- API routers are registered in `src/api/api.py` and individual routes live in `src/api/routes/`.
- Follow the existing router pattern when adding new feature areas (create a new file under `routes` and include it in `api.py`).

## Contributing

Contributions are welcome. Open a PR with a descriptive title and tests when applicable.

## License

This project is provided as-is. Add a license file if you intend to reuse or publish.

