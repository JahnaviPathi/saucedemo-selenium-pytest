import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"
WAIT_TIMEOUT = 10  # Maximum seconds to wait for elements


@pytest.fixture
def driver():
    """Start Chrome automatically via Selenium Manager and close it after each test."""
    options = webdriver.ChromeOptions()
    # Uncomment the next line to run Chrome in the background without a visible window
    # options.add_argument("--headless=new")

    # Selenium 4.6+ automatically downloads and manages ChromeDriver
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser  # Pass the browser to the test
    browser.quit()  # Always close the browser when the test finishes


def login(driver, username, password):
    """Helper function to open SauceDemo and submit the login form."""
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    # Wait for the username, password, and login button, then interact
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    if username:
        username_input.send_keys(username)
    if password:
        password_input.send_keys(password)
    login_button.click()


def test_valid_login(driver):
    """Test 1: Verify a valid user can log in and reach the products page."""
    login(driver, "standard_user", "secret_sauce")

    # Wait until the URL changes to the inventory (products) page
    WebDriverWait(driver, WAIT_TIMEOUT).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url, (
        f"Expected URL to contain 'inventory.html', but got: {driver.current_url}"
    )


def test_login_wrong_password(driver):
    """Test 2: Verify an error message appears when entering a wrong password."""
    login(driver, "standard_user", "wrong_password")

    # Wait for the error banner to appear
    error_banner = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert "do not match any user" in error_banner.text.lower(), (
        f"Unexpected error message: '{error_banner.text}'"
    )


def test_login_empty_username(driver):
    """Test 3: Verify an error message appears when submitting an empty username."""
    login(driver, "", "secret_sauce")

    # Wait for the validation error banner
    error_banner = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert "username is required" in error_banner.text.lower(), (
        f"Unexpected error message: '{error_banner.text}'"
    )


def test_products_page_shows_items(driver):
    """Test 4: Verify the products page displays product items after login."""
    login(driver, "standard_user", "secret_sauce")

    # Wait until at least one product card is visible on the inventory page
    products = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert len(products) > 0, "Expected products to be displayed, but found 0 items."


def test_add_product_updates_cart_count(driver):
    """Test 5: Verify adding a product to the cart updates the cart badge count to 1."""
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    # Wait for the first 'Add to cart' button and click it
    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_button.click()

    # Wait for the cart badge to appear and check that it shows '1'
    cart_badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1", (
        f"Expected cart count '1', but got: '{cart_badge.text}'"
    )
  
