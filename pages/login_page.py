from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def login(self, username, password):
        self.browser.get("https://www.saucedemo.com/")

        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()

        # Tunggu sampai halaman inventory terbuka
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
