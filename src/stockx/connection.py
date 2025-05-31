# Local Imports
from .secure import secure_call

# External Imports
import httpx

API_KEY = None
JWT = None
REFRESH_TOKEN = None
CLIENT_ID = None
CLIENT_SECRET = None
HEADERS = {}


def setup(config: dict):
    """
    Initializes the global authentication headers for making requests to the StockX API.

    This function must be called before making any API requests that require authentication.
    It sets global variables used for authentication, including the API key, JWT, and headers.

    Parameters
    ----------
    config : dict
        A dictionary containing authentication and configuration values. Expected keys:
            - api_key (str): Your StockX API key used to authenticate the request.
            - jwt (str): A valid JSON Web Token (JWT) used for bearer authorization.
            - refresh_token (str, optional): Refresh token for renewing JWTs.
            - client_id (str, optional): Client ID used in the token refresh process.
            - client_secret (str, optional): Client secret used in the token refresh process.

    Side Effects
    ------------
    Sets the global variables:
        - API_KEY: Stores the provided API key.
        - JWT: Stores the provided JWT.
        - REFRESH_TOKEN: Stores the refresh token.
        - CLIENT_ID: Stores the client ID.
        - CLIENT_SECRET: Stores the client secret.
        - HEADERS: Dictionary containing required headers for authenticated HTTP requests.
    """

    global API_KEY, JWT, REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET, HEADERS

    API_KEY = config.get("api_key", "")
    JWT = config.get("jwt", "")
    REFRESH_TOKEN = config.get("refresh_token", "")
    CLIENT_ID = config.get("client_id", "")
    CLIENT_SECRET = config.get("client_secret", "")
    HEADERS = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
        "Authorization": f"Bearer {JWT}",
    }


@secure_call()
async def execute(url: str, params: dict = {}):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params, headers=HEADERS)
        return resp.json()


@secure_call()
async def execute_post(url: str, data: dict = {}):
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, data=data, headers=HEADERS)
        return resp.json()


@secure_call()
async def refresh_tokens():
    """
    Refreshes the JWT access token using the OAuth 2.0 refresh token flow.

    This function sends a POST request to the StockX OAuth token endpoint using stored
    credentials (client ID, client secret, and refresh token) to obtain a new access token.
    The function assumes that these values have already been set globally via the `setup()` function.

    Returns
    -------
    dict
        A dictionary containing the new access token and related metadata, such as:
            - access_token (str): The new JWT for authenticated requests.
            - token_type (str): Typically 'Bearer'.
            - expires_in (int): Token validity duration in seconds.
            - scope (str): Scopes associated with the token (if provided).

    Raises
    ------
    httpx.HTTPStatusError
        If the request fails due to invalid credentials or network issues.
    """
    url = "https://accounts.stockx.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": "gateway.stockx.com",
        "refresh_token": REFRESH_TOKEN,
    }

    return await execute_post(url, data)
