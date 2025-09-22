import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-save-password-bubble")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def close_password_popup_if_any(driver):
    """
    Helper untuk menutup popup Google Password Manager
    kalau muncul setelah login.
    """
    try:
        popup_ok = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
        )
        popup_ok.click()
        print("✅ Popup password manager tertutup.")
    except TimeoutException:
        print("ℹ️ Tidak ada popup password manager.")
