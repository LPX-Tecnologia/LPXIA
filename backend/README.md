# LPXIA Backend

Backend em **FastAPI**, pronto para rodar local ou via Docker.

## Estrutura

```
backend/
├── requirements.txt
├── .env.example
├── Dockerfile
├── README.md
└── app/
    ├── __init__.py
    ├── main.py          # instancia e configura o FastAPI
    ├── config.py         # Settings (variáveis de ambiente)
    ├── lifespan.py        # eventos de startup/shutdown
    ├── api/
    │   ├── __init__.py    # agrega os routers em api_router
    │   └── health.py      # endpoints /health e /health/ready
    ├── core/
    │   ├── __init__.py
    │   └── ai_client.py   # stub local de IA (sem dependência de quota)
    └── utils/
        ├── __init__.py
        └── time.py
```

## Rodando localmente

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Docs (Swagger): http://localhost:8000/docs
- Health check: http://localhost:8000/api/v1/health

## Rodando com Docker

```bash
cd backend
docker build -t lpxia-backend .
docker run --rm -p 8000:8000 --env-file .env.example lpxia-backend
```

## Variáveis de ambiente

Veja `.env.example`. Nenhuma é obrigatória para o backend subir — sem
`OPENAI_API_KEY`, o `app/core/ai_client.py` usa automaticamente um stub
local (`StubAIClient`) que não faz chamadas externas e não depende de quota.
Preencha `OPENAI_API_KEY` quando quiser habilitar a integração real com a
OpenAI (nesse caso, adicione também o pacote `openai` ao `requirements.txt`).

## Testes rápidos

```bash
curl http://localhost:8000/api/v1/health
curl http://localhost:8000/
```
