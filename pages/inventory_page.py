from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)

    def add_first_product_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button.btn_inventory"))
        )
        add_button.click()

        # Tunggu cart badge muncul
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
        )

    def remove_first_product_from_cart(self):
        remove_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']"))
        )
        remove_button.click()

        # Tunggu cart badge hilang
        self.wait.until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
