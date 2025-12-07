from fastapi import APIRouter, Request
import subprocess
import json

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
@cache_decorator(expire=86_400) # Daily
async def get_exchanges():
    subprocess.run(
        ["python", "-m", "scrapy", "crawl", "exchanges", "-O", "data.json"], 
        cwd=r"C:\Users\THINKPAD\Desktop\Flutter TP\ExchangeCrawler"
    )

    with open("ExchangeCrawler/data.json", "r") as file:
        data = json.load(file)

    return data
