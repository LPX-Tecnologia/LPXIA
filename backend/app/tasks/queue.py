from app.redis.client import RedisClient


class TaskQueue:
    def __init__(self, redis_client: RedisClient | None = None):
        self.redis_client = redis_client or RedisClient()

    def enqueue(self, queue_name: str, payload: dict) -> None:
        self.redis_client.push_queue(queue_name, payload)

    def dequeue(self, queue_name: str) -> dict | None:
        value = self.redis_client.pop_queue(queue_name)
        return value if isinstance(value, dict) else None
