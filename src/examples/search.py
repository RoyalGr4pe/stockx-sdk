from stockx.search import search
from stockx.connection import setup

import asyncio

API_KEY = "STOCK-X-API-KEY"
JWT = "STOCK-X-JWT"
setup({"api_key": API_KEY, "jwt": JWT})


async def search_query():
    params = {
        "query": "CU9225-001"
    }
    result = await search(params)
    print("Seach Results", result)


if __name__ == "__main__":
    asyncio.run(search_query())
