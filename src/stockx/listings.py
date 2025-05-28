# Local Imports
from .secure import secure_call
from .connection import execute


@secure_call
async def get_all_listings(params: dict):
    """
    Retrieve a paginated list of selling listings from the StockX API.

    This function wraps an HTTP GET request to the `/v2/selling/listings` endpoint,
    applying any query parameters provided in the `params` dictionary. The `secure_call`
    decorator handles authentication and error‐handling boilerplate.

    Parameters
    ----------
    params : dict
        A dictionary of optional query parameters to filter and paginate results.
        Recognized keys include:

        - **pageNumber** (int):
          The page number to retrieve. Must be greater than or equal to 1.
          Defaults to 1.
          Example: `pageNumber=1`

        - **pageSize** (int):
          The number of listings to return per page. Must be between 1 and 100.
          Defaults to 1.
          Example: `pageSize=100`

        - **productIds** (str):
          Comma-separated list of product IDs.
          Do not include array brackets (`[]`) or quotation marks (`"` or `'`).
          Example: `productIds=abc123,def456`

        - **variantIds** (str):
          Comma-separated list of variant IDs.
          Do not include array brackets (`[]`) or quotation marks (`"` or `'`).
          Example: `variantIds=var1,var2`

        - **batchIds** (str):
          Comma-separated list of batch IDs.
          Do not include array brackets (`[]`) or quotation marks (`"` or `'`).
          Example: `batchIds=batchA,batchB`

        - **fromDate** (str):
          Start date of the query.
          Format: `YYYY-MM-DD`
          Example: `fromDate=2022-06-08`

        - **toDate** (str):
          End date of the query.
          Format: `YYYY-MM-DD`
          Example: `toDate=2022-06-08`

        - **listingStatuses** (str):
          Comma-separated list of listing statuses.
          Valid values include: `"INACTIVE"`, `"ACTIVE"`, `"DELETED"`, `"CANCELED"`, `"MATCHED"`, `"COMPLETED"`
          Do not include array brackets or quotation marks.
          Example: `listingStatuses=ACTIVE,COMPLETED`

        - **inventoryTypes** (str):
          Comma-separated list of inventory types. Valid values are `"STANDARD"` or `"FLEX"`.
          Do not include brackets or quotes.
          Example: `inventoryTypes=STANDARD,FLEX`

        - **initiatedShipmentDisplayIds** (str):
          Shipment display IDs associated with the listing.
          These are the same IDs generated when a Flex inbound list is created in StockX Pro.

    Returns
    -------
    dict
        The parsed JSON response as a Python dictionary containing listing data.
        Raises an HTTPError if the response status is not in the 200–299 range.
    """
    query = {
        "pageNumber": params.get("pageNumber", 1),
        "pageSize": params.get("pageSize", 1),
        "productIds": params.get("productIds", ""),
        "variantIds": params.get("variantIds", ""),
        "batchIds": params.get("batchIds", ""),
        "fromDate": params.get("fromDate", ""),
        "toDate": params.get("toDate", ""),
        "listingStatuses": params.get("listingStatuses", ""),
        "inventoryTypes": params.get("inventoryTypes", ""),
        "initiatedShipmentDisplayIds": params.get("initiatedShipmentDisplayIds", ""),
    }

    url = "https://api.stockx.com/v2/selling/listings"

    return await execute(url, query)

@secure_call
async def get_single_listing(listingId: str):
    """
    Retrieve details for a single selling listing by its unique identifier from the StockX API.

    Parameters
    ----------
    listingId : str
        The unique UUID of the listing to retrieve (e.g. `"98e2e748-8000-45bf-a624-5531d6a68318"`).

    Returns
    -------
    dict
        The parsed JSON response containing the listing details.

    Raises
    ------
    httpx.HTTPStatusError
        If the HTTP response status code is not in the 200–299 range.
    """
    url = f"https://api.stockx.com/v2/selling/listings/{listingId}"

    return await execute(url)
