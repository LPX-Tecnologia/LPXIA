import os
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")

from app.main import app


@pytest.fixture()
def client() -> TestClient:
    with TestClient(app) as test_client:
        yield test_client


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_register_user(client: TestClient) -> None:
    email = f"{uuid4().hex}@example.com"
    payload = {"email": email, "password": "strong-password"}
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 201


def test_login_user(client: TestClient) -> None:
    email = f"{uuid4().hex}@example.com"
    payload = {"email": email, "password": "strong-password"}
    client.post("/api/v1/auth/register", json=payload)
    response = client.post("/api/v1/auth/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()


def test_refresh_token_flow(client: TestClient) -> None:
    email = f"{uuid4().hex}@example.com"
    payload = {"email": email, "password": "strong-password"}
    client.post("/api/v1/auth/register", json=payload)
    login_response = client.post("/api/v1/auth/login", json=payload)
    refresh_token = login_response.json()["refresh_token"]

    response = client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_admin_endpoint_requires_admin_role(client: TestClient) -> None:
    email = f"{uuid4().hex}@example.com"
    payload = {"email": email, "password": "strong-password"}
    client.post("/api/v1/auth/register", json=payload)
    login_response = client.post("/api/v1/auth/login", json=payload)
    token = login_response.json()["access_token"]

    response = client.get(
        "/api/v1/auth/admin",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403
