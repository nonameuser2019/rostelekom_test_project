from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthByCodePage(BasePage):
    BASE_URL = 'https://lk.rt.ru/'

    def __init__(self, browser, timeout=10):
        super().__init__(browser, timeout)
        self.url = self.BASE_URL

    def open(self):
        super().open()
        return self

    def enter_with_password_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button[name='standard_auth_btn']")

    def click_on_enter_with_password_btn(self):
        from pages.auth_by_password_page import AuthByPasswordPage
        self.enter_with_password_btn().click()
        return AuthByPasswordPage(self.browser)
