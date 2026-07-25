# Backend

This backend uses FastAPI, SQLAlchemy, Alembic, PostgreSQL, Redis and JWT authentication.

## Environment

Copy the sample environment file and update it:

```bash
cp .env.example .env
```

## Database

Run migrations:

```bash
alembic upgrade head
```

Run seeds:

```bash
python -c "from app.seeders.run_seed import run_seed; run_seed()"
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest -q
```
