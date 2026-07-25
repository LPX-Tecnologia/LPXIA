from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_memory_flow() -> None:
    payload = {"email": "memory@example.com", "password": "strong-password"}
    register = client.post("/api/v1/auth/register", json=payload)
    assert register.status_code == 201

    login = client.post("/api/v1/auth/login", json=payload)
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    memory_payload = {"title": "Preference", "content": "User prefers concise answers", "memory_type": "preference"}
    create_response = client.post("/api/v1/memory/", json=memory_payload, headers=headers)
    assert create_response.status_code == 201

    list_response = client.get("/api/v1/memory/", headers=headers)
    assert list_response.status_code == 200
    assert len(list_response.json()) >= 1
