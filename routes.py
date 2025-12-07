from fastapi import APIRouter
import subprocess
import json

from main import cache_decorator

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
