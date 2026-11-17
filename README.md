# SauceDemo — Selenium + PyTest Test Automation

A beginner-friendly test automation project using **Python**, **Selenium 4**, and **PyTest** to test core login and shopping cart flows on [https://www.saucedemo.com](https://www.saucedemo.com).

## Project Structure

```text
.
├── tests/
│   └── test_saucedemo.py
├── requirements.txt
└── README.md
```

## What Is Tested

1. **Valid Login (`test_valid_login`)** — Logs in with `standard_user` / `secret_sauce` and verifies the browser navigates to `inventory.html`.
2. **Wrong Password (`test_login_wrong_password`)** — Enters an invalid password and verifies the expected error banner is shown.
3. **Empty Username (`test_login_empty_username`)** — Submits the login form without a username and verifies the `"Username is required"` error message appears.
4. **Products Page Items (`test_products_page_shows_items`)** — Logs in and confirms product cards are visible on the inventory page.
5. **Add to Cart (`test_add_product_updates_cart_count`)** — Clicks **Add to cart** on a product and verifies the shopping cart badge updates to `1`.

## Prerequisites

- Python 3.9 or higher
- Google Chrome installed (Selenium 4's built-in **Selenium Manager** automatically downloads and manages ChromeDriver—no manual driver setup needed)

## Installation

1. Create and activate a virtual environment:

   **Windows (Command Prompt / PowerShell):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS / Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run Tests

Run all tests with verbose output:

```bash
pytest -v
```

## Sample Output

```text
========================= test session starts ==========================
platform win32 -- Python 3.11.6, pytest-8.3.3, pluggy-1.5.0
collected 5 items

tests/test_saucedemo.py::test_valid_login PASSED                  [ 20%]
tests/test_saucedemo.py::test_login_wrong_password PASSED         [ 40%]
tests/test_saucedemo.py::test_login_empty_username PASSED         [ 60%]
tests/test_saucedemo.py::test_products_page_shows_items PASSED    [ 80%]
tests/test_saucedemo.py::test_add_product_updates_cart_count PASSED [100%]

========================== 5 passed in 11.45s ==========================
```
