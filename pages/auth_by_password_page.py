from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthByPasswordPage(BasePage):

    def register_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, "a#kc-register")

    def click_register_link(self):
        from pages.register_page import RegisterPage
        self.register_link().click()
        return RegisterPage(self.browser)


