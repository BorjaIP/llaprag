
import redis
from llama_index.core.storage.index_store.keyval_index_store import KVIndexStore
from llama_index.storage.index_store.redis import RedisIndexStore

from llaprag.settings import settings


class IndexRedis:
    """Initializes the Redis Index Store."""

    def __init__(self):

        # Index store for metadata
        # https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/
        redis_url = f"redis://:{settings.redis.password}@{settings.redis.host}:{settings.redis.port}/{settings.redis.namespace}"
        redis_client = redis.Redis(
            host=settings.redis.host, port=settings.redis.port, password=settings.redis.password
        )
        self.redis_store: KVIndexStore = RedisIndexStore.from_redis_client(
            redis_client=redis_client, namespace=settings.redis.namespace
        )
