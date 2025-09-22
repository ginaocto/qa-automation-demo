from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_and_remove_product(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)

    # Add to cart
    inventory.add_first_product_to_cart()
    browser.save_screenshot("reports/after_add.png")

    # Remove from cart
    inventory.remove_first_product_from_cart()
    browser.save_screenshot("reports/after_remove.png")
