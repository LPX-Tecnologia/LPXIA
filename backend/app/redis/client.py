import json
from typing import Any

import redis

from app.core.config import get_settings

settings = get_settings()
client = redis.Redis.from_url(settings.redis_url, decode_responses=True)


class RedisClient:
    def __init__(self, connection: redis.Redis | None = None):
        self.connection = connection or client

    def set_value(self, key: str, value: Any, ttl: int | None = None) -> None:
        payload = json.dumps(value) if not isinstance(value, str) else value
        self.connection.set(key, payload, ex=ttl)

    def get_value(self, key: str) -> Any | None:
        value = self.connection.get(key)
        if value is None:
            return None
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    def delete_value(self, key: str) -> None:
        self.connection.delete(key)

    def push_queue(self, queue_name: str, value: Any) -> None:
        payload = json.dumps(value) if not isinstance(value, str) else value
        self.connection.rpush(queue_name, payload)

    def pop_queue(self, queue_name: str) -> Any | None:
        value = self.connection.lpop(queue_name)
        if value is None:
            return None
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    def set_session(self, session_id: str, value: Any, ttl: int = 3600) -> None:
        self.set_value(f"session:{session_id}", value, ttl=ttl)

    def get_session(self, session_id: str) -> Any | None:
        return self.get_value(f"session:{session_id}")
