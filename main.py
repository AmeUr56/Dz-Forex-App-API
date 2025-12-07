from fastapi import FastAPI, Request

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import redis

cache_decorator = cache
def create_app():
    # Initialize FastAPI app
    app = FastAPI(
        title="Exchange-App-API",
        description="",
        version="1.0.0"
    )

    # Caching
    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    app.state.cache = FastAPICache


    # Include the routers in the app
    from routes import main_router, exchanges_router
    app.include_router(main_router)
    app.include_router(exchanges_router)

    return app