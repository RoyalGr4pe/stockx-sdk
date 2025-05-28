import httpx

API_KEY = None
JWT     = None
HEADERS = {}

def setup(api_key: str, jwt: str):
    """
    Initializes the global authentication headers for making requests to the StockX API.

    This function must be called before making any API requests that require authentication.
    It sets global variables used for authentication, including the API key, JWT, and headers.

    Parameters
    ----------
    api_key : str
        Your StockX API key used to authenticate the request.
    
    jwt : str
        A valid JSON Web Token (JWT) used for bearer authorization.

    Side Effects
    ------------
    Sets the global variables:
        - API_KEY: Stores the provided API key.
        - JWT: Stores the provided JWT.
        - HEADERS: Dictionary containing required headers for authenticated HTTP requests.
    """

    global API_KEY, JWT, HEADERS

    API_KEY = api_key
    JWT     = jwt
    HEADERS = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
        "Authorization": f"Bearer {JWT}"
    }


async def execute(url: str, params: dict = {}):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
