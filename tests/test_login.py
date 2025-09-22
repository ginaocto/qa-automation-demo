from pages.login_page import LoginPage

def test_valid_login(browser):
    login = LoginPage(browser)
    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in browser.current_url.lower(), "Login gagal, tidak diarahkan ke inventory page"
