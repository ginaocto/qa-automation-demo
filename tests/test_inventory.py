import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from conftest import close_password_popup_if_any

def test_add_and_remove_product(browser):
    # Login
    login = LoginPage(browser)
    login.open()
    login.login("standard_user", "secret_sauce")
    close_password_popup_if_any(browser)

    inventory = InventoryPage(browser)

    # Add product
    inventory.add_first_product_to_cart()
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element(inventory.cart_icon, "1")
    )
    assert inventory.get_cart_count() == "1"
    time.sleep(2)

    # Remove product
    inventory.remove_first_product_from_cart()

    # 🔹 Tambahan: tunggu cart badge hilang
    WebDriverWait(browser, 3).until_not(
        EC.presence_of_element_located(inventory.cart_icon)
    )
    assert inventory.get_cart_count() == "0"
    time.sleep(2)
