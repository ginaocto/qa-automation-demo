from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_product_to_cart(self):
        add_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]"))
        )
        add_button.click()

    def remove_first_product_from_cart(self):
        remove_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text()='Remove'])[1]"))
        )
        remove_button.click()

        # 🔹 Tambahan: tunggu tombol balik ke "Add to cart"
        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element((By.XPATH, "(//button)[1]"), "Add to cart")
        )

    def get_cart_count(self):
        try:
            cart_count = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.cart_icon)
            )
            return cart_count.text
        except:
            return "0"
