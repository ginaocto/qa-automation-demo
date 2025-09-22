from pages.login_page import LoginPage

def test_login(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    # Screenshot hasil login
    browser.save_screenshot("reports/after_login.png")
