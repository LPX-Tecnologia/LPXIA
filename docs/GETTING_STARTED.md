# Getting Started

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Node.js 20+

## Backend

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Full stack with Docker

```bash
docker compose up --build
```
