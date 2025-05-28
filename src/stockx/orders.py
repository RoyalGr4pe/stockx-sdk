# Local Imports
from .secure import secure_call
from .connection import execute


@secure_call
async def get_active_orders(params: dict):
    """
    Retrieve the current user’s active orders from the StockX API.

    This function sends an authenticated GET request to the `/v2/selling/orders/active`
    endpoint, applying any pagination, filtering, or sorting options supplied.

    Parameters
    ----------
    params : dict
        A dictionary of optional query parameters:

        - **pageNumber** (int):
          The page number to retrieve, starting from 1. Must be an integer greater than or equal to 1.

        - **pageSize** (int):
          The number of results to return per page. Must be an integer between 1 and 100.

        - **orderStatus** (str):
          Filter orders by status. Valid values include:
          `"CREATED"`, `"CCAUTHORIZATIONFAILED"`, `"SHIPPED"`, `"RECEIVED"`, `"AUTHENTICATING"`,
          `"AUTHENTICATED"`, `"PAYOUTPENDING"`, `"PAYOUTCOMPLETED"`, `"SYSTEMFULFILLED"`,
          `"PAYOUTFAILED"`, `"SUSPENDED"`.
          Example: `orderStatus="CREATED"`

        - **productId** (str):
          Unique identifier for a product.

        - **variantId** (str):
          Unique identifier for a product’s variant.

        - **sortOrder** (str):
          Determines how the results are sorted.
          Default is `"CREATEDAT"`. Another valid option is `"SHIPBYDATE"`.

        - **inventoryTypes** (str):
          Comma-separated list of inventory types. Valid values are `"STANDARD"` or `"FLEX"`.
          Do not include brackets or quotes.
          Example: `inventoryTypes=STANDARD,FLEX`

        - **initiatedShipmentDisplayIds** (str):
          Shipment display IDs associated with the orders.
          This ID is the same as the one generated when a Flex inbound list is created in StockX Pro.

    Returns
    -------
    dict
        The parsed JSON response as a Python dictionary containing the active order data.

    Raises
    ------
    httpx.HTTPStatusError
        If the HTTP response status code is not in the 200–299 range.
    """
    query = {
        "pageNumber": params.get("pageNumber", 1),
        "pageSize": params.get("pageSize", 1),
        "orderStatus": params.get("orderStatus", ""),
        "productId": params.get("productId", ""),
        "variantId": params.get("variantId", ""),
        "sortOrder": params.get("sortOrder", ""),
        "inventoryTypes": params.get("inventoryTypes", ""),
        "initiatedShipmentDisplayIds": params.get("initiatedShipmentDisplayIds", ""),
    }

    url = "https://api.stockx.com/v2/selling/orders/active"

    return await execute(url, query)


@secure_call
async def get_historical_orders(params: dict):
    """
    Retrieve the user’s historical orders from the StockX API.

    This function sends an authenticated GET request to the `/v2/selling/orders/history`
    endpoint, applying any filters, pagination, and sorting options supplied.

    Parameters
    ----------
    params : dict
        A dictionary of optional query parameters:

        - **fromDate** (str):
          The start date to filter orders created on or after this date.
          Format: `YYYY-MM-DD`. Defaults to no lower bound.

        - **toDate** (str):
          The end date to filter orders created on or before this date.
          Format: `YYYY-MM-DD`. Defaults to no upper bound.

        - **pageNumber** (int):
          The requested page number to retrieve. Must be greater than or equal to 1.
          Defaults to `1`.
          Example: `pageNumber=1`

        - **pageSize** (int):
          Number of orders to return per page. Must be between 1 and 100.
          Defaults to `10`.
          Example: `pageSize=100`

        - **orderStatus** (str):
          Filter historical orders by status. Valid values include:
          `"AUTHFAILED"`, `"DIDNOTSHIP"`, `"CANCELED"`, `"COMPLETED"`, `"RETURNED"`
          Example: `orderStatus=CANCELED`

        - **productId** (str):
          Unique StockX product ID to filter the results.

        - **variantId** (str):
          Unique StockX variant ID to filter the results.

        - **inventoryTypes** (str):
          Comma-separated list of inventory types. Valid values are `"STANDARD"` or `"FLEX"`.
          Do not use brackets or quotes.
          Example: `inventoryTypes=STANDARD,FLEX`

        - **initiatedShipmentDisplayIds** (str):
          The shipment's unique display ID associated with the order.
          This is the same ID generated when a Flex inbound list is created in StockX Pro.

    Returns
    -------
    dict
        The parsed JSON response as a Python dictionary containing the historical order data.

    Raises
    ------
    httpx.HTTPStatusError
        If the HTTP response status code is not in the 200–299 range.
    """
    query = {
        "fromDate": params.get("fromDate", ""),
        "toDate": params.get("toDate", ""),
        "pageNumber": params.get("pageNumber", 1),
        "pageSize": params.get("pageSize", 20),
        "orderStatus": params.get("orderStatus", ""),
        "productId": params.get("productId", ""),
        "variantId": params.get("variantId", ""),
        "inventoryTypes": params.get("inventoryTypes", ""),
        "initiatedShipmentDisplayIds": params.get("initiatedShipmentDisplayIds", ""),
    }

    url = "https://api.stockx.com/v2/selling/orders/history"

    return await execute(url, query)


@secure_call
async def get_single_order(order_number: str):
    """
    Retrieve details for a single order by its StockX order number.

    Parameters
    ----------
    order_number : str
        The unique StockX order number (e.g. "323314425-323214184").

    Returns
    -------
    dict
        The parsed JSON response as a Python dictionary containing the order details.

    Raises
    ------
    httpx.HTTPStatusError
        If the HTTP response status code is not in the 200–299 range.
    """
    url = f"https://api.stockx.com/v2/selling/orders/{order_number}"

    return await execute(url)
