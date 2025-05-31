# Local IMports# Local Imports
from .secure import secure_call
from .connection import execute


@secure_call()
async def search(params: dict):
    """
    Performs a search query against the StockX product catalog.

    Sends a GET request to the StockX catalog search endpoint with the specified query parameters.
    This allows searching for products by keyword and paginating through results.

    Parameters
    ----------
    params : dict
        A dictionary of search parameters. Expected keys:
            - query (str): The search keyword or phrase.
            - pageNumber (int, optional): The page number for pagination (default is 1).
            - pageSize (int, optional): The number of results per page (default is 1).

    Returns
    -------
    dict
        A dictionary containing the search results, including product metadata and pagination info.

    Raises
    ------
    httpx.HTTPStatusError
        If the request to the StockX API fails.
    """
    query = {
        "query": params.get("query", 1),
        "pageNumber": params.get("pageNumber", 1),
        "pageSize": params.get("pageSize", 1),
    }

    url = "https://api.stockx.com/v2/catalog/search"

    return await execute(url, query)
