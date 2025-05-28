from stockx.orders import get_active_orders, get_historical_orders, get_single_order
from stockx.connection import setup

import asyncio

API_KEY = "STOCK-X-API-KEY"
JWT = "STOCK-X-JWT"

setup(API_KEY, JWT)


async def active_orders():
    params = {"pageNumber": 1, "pageSize": 5, "orderStatus": "CREATED"}
    result = await get_active_orders(params)
    print("Active Orders Result:", result)


async def historical_orders():
    params = {
        "fromDate": "2023-01-01",
        "toDate": "2023-04-01",
        "pageNumber": 1,
        "pageSize": 10,
        "orderStatus": "CANCELED",
        "productId": "12345",
        "variantId": "67890",
        "inventoryTypes": "STANDARD",
        "initiatedShipmentDisplayIds": "SHIP123",
    }
    result = await get_historical_orders(params)
    print("Historical Orders:", result)


async def single_order():
    order_number = "323314425-323214184"
    result = await get_single_order(order_number)
    print("Single Order Details:", result)


async def main():
    await active_orders()
    await historical_orders()
    await single_order()


if __name__ == "__main__":
    asyncio.run(main())
