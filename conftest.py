import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()

    # Matikan password manager & save bubble
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    # Gunakan fresh profile (tanpa history & tanpa save password)
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
