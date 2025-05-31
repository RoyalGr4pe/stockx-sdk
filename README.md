# StockX SDK

A Python SDK for seamless interaction with the StockX Marketplace API. This SDK provides a simplified and secure interface to programmatically interact with StockX's selling features, including listings and order management.

---

## 📦 Installation

```
pip install stockx
```

---

## 🛠 Setup

Before calling any functions, you must configure the SDK with your API key and JWT token:

```python
from stockx.connection import setup

setup(api_key="YOUR_API_KEY", jwt="YOUR_JWT_TOKEN")
```

---

## 🔍 Functions

### `get_all_listings(params: dict)`

Fetch all listings based on various filters.

#### Parameters:
- `pageNumber` (int): The requested page number. Starts at 1.
- `pageSize` (int): Number of listings per page.
- `productIds` (str): Comma-separated product IDs.
- `variantIds` (str): Comma-separated variant IDs.
- `batchIds` (str): Comma-separated batch IDs.
- `fromDate` (str): Start date in `YYYY-MM-DD` format.
- `toDate` (str): End date in `YYYY-MM-DD` format.
- `listingStatuses` (str): Listing statuses (e.g., `ACTIVE`).
- `inventoryTypes` (str): `STANDARD` or `FLEX`.
- `initiatedShipmentDisplayIds` (str): Unique shipment display IDs.

#### Returns:
`dict` – JSON response containing listing data.

---

### `get_single_listing(listingId: str)`

Fetch a single listing by its ID.

#### Parameters:
- `listingId` (str): The unique ID of the listing.

#### Returns:
`dict` – JSON response of the listing.

---

### `get_active_orders(params: dict)`

Fetch active orders using optional filters.

#### Parameters:
- `pageNumber` (int): Page number to retrieve.
- `pageSize` (int): Number of results per page.
- `orderStatus` (str): Status filter (`CREATED`, `SHIPPED`, etc.).
- `productId` (str): StockX product ID.
- `variantId` (str): StockX variant ID.
- `sortOrder` (str): Sort field (`CREATEDAT`, `SHIPBYDATE`).
- `inventoryTypes` (str): Comma-separated list, e.g., `STANDARD`.
- `initiatedShipmentDisplayIds` (str): Shipment display ID.

#### Returns:
`dict` – JSON response with active orders.

---

### `get_order_history(params: dict)`

Fetch historical orders using filters and date range.

#### Parameters:
- `fromDate` (str): Start date (`YYYY-MM-DD`).
- `toDate` (str): End date (`YYYY-MM-DD`).
- `pageNumber` (int): Page number (default: 1).
- `pageSize` (int): Page size (default: 10).
- `orderStatus` (str): Historical status (`CANCELED`, `COMPLETED`, etc.).
- `productId` (str): Product ID.
- `variantId` (str): Variant ID.
- `inventoryTypes` (str): `STANDARD`, `FLEX`.
- `initiatedShipmentDisplayIds` (str): Shipment display ID.

#### Returns:
`dict` – JSON response with order history.

---

### `get_single_order(orderNumber: str)`

Fetch a specific order by order number.

#### Parameters:
- `orderNumber` (str): The unique order number to fetch.

#### Returns:
`dict` – JSON response with order details.

---

### `search(params: dict)`

Search the StockX product catalog using a keyword and optional pagination.

#### Parameters:
- `query` (str): Search term (e.g., product name, style code).
- `pageNumber` (int): Page number of results to retrieve (default: 1).
- `pageSize` (int): Number of results per page (default: 1).

#### Returns:
`dict` – JSON response containing matched products and pagination metadata.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Created by [Nick](mailto:njames.programming@gmail.com). Contributions welcome!
