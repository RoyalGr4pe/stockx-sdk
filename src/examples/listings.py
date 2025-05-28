from stockx.listings import get_all_listings, get_single_listing
from stockx.connection import setup

import asyncio

API_KEY = "STOCK-X-API-KEY"
JWT = "STOCK-X-JWT"

setup(API_KEY, JWT)


async def all_listings():
    params = {
        "pageNumber": 1,
        "pageSize": 5,
        "productIds": "abc123,def456",
        "variantIds": "var1,var2",
        "batchIds": "batchA,batchB",
        "fromDate": "2022-01-01",
        "toDate": "2022-12-31",
        "listingStatuses": "ACTIVE,COMPLETED",
        "inventoryTypes": "STANDARD,FLEX",
        "initiatedShipmentDisplayIds": "SHIP123",
    }
    result = await get_all_listings(params)
    print("All Listings:", result)


async def single_listing():
    listing_id = "98e2e748-8000-45bf-a624-5531d6a68318"
    result = await get_single_listing(listing_id)
    print("Single Listing:", result)


async def main():
    await all_listings()
    await single_listing()


if __name__ == "__main__":
    asyncio.run(main())
