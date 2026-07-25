from app.redis.client import RedisClient


class FakeRedis:
    def __init__(self) -> None:
        self.store: dict[str, tuple[str, int | None]] = {}
        self.queues: dict[str, list[str]] = {}

    def set(self, key: str, value: str, ex: int | None = None) -> bool:
        self.store[key] = (value, ex)
        return True

    def get(self, key: str) -> str | None:
        item = self.store.get(key)
        return item[0] if item else None

    def delete(self, key: str) -> None:
        self.store.pop(key, None)

    def rpush(self, key: str, value: str) -> None:
        self.queues.setdefault(key, []).append(value)

    def lpop(self, key: str) -> str | None:
        items = self.queues.get(key)
        if not items:
            return None
        return items.pop(0)


def test_redis_client_roundtrip_and_queue() -> None:
    fake_connection = FakeRedis()
    client = RedisClient(connection=fake_connection)

    client.set_value("foo", "bar", ttl=5)
    assert client.get_value("foo") == "bar"

    client.set_session("abc", {"user": "x"}, ttl=10)
    assert client.get_session("abc") == {"user": "x"}

    client.push_queue("tasks", {"id": 1})
    assert client.pop_queue("tasks") == {"id": 1}

    client.delete_value("foo")
    assert client.get_value("foo") is None
