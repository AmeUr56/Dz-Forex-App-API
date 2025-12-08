from fastapi import APIRouter, Request
import subprocess
import json
import os

from main import cache_decorator

# Main Router
main_router = APIRouter(prefix="", tags=["main"])


@main_router.get("/")
@main_router.head("/")
async def home(request: Request):
    return "Welcome to Dz Forex"


# Exchanges Router
exchanges_router = APIRouter(prefix="/exchanges", tags=["exchanges"])

@exchanges_router.get("/",
        summary="Get Exchanges",
        description="Get Multiple Currencies Exchange.")
#@cache_decorator(expire=86_400) # Daily
async def get_exchanges():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CRAWLER_DIR = os.path.join(BASE_DIR, "ExchangeCrawler")
    DATA_FILE = os.path.join(BASE_DIR, "ExchangeCrawler", "data.json")

    subprocess.run(
        ["python", "-m", "scrapy", "crawl", "exchanges", "-O", DATA_FILE],
        cwd=CRAWLER_DIR
    )

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return data
