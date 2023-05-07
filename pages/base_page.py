from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, browser: webdriver.Chrome, timeout=10):
        self.browser = browser
        self.url = None
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def url_should_have(self, url: str):
        assert url in self.browser.current_url, f'Неверный URL адрес страницы'
