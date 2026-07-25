# Contributing to LPX-NEXUS

Thank you for contributing to LPX-NEXUS.

## Development workflow

1. Fork the repository and create a feature branch.
2. Keep changes focused and well-documented.
3. Add or update tests when behavior changes.
4. Run the relevant backend tests before opening a pull request.
5. Open a pull request with a clear summary and scope.

## Code standards

- Follow clean code and modular architecture principles.
- Keep modules scoped and easy to extend.
- Prefer explicit configuration over hardcoded values.
- Document new features and public APIs.

## Running locally

- Backend: `cd backend && python -m pip install -r requirements.txt`
- Frontend: `cd frontend && npm install && npm run dev`
- Infrastructure: `docker compose up --build`
