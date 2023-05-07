from pages.auth_by_code_page import AuthByCodePage
from data.test_data import wrong_password
import pytest


class TestRegistration:

    @staticmethod
    def register_page(browser):
        code_auth_page = AuthByCodePage(browser).open()
        pass_auth_page = code_auth_page.click_on_enter_with_password_btn()
        register_page = pass_auth_page.click_register_link()
        return register_page

    @pytest.mark.xfail(reason="Текст на кнопке не соответствует ожидаемому")
    def test_check_all_fields(self, browser):
        register_page = self.register_page(browser)
        register_page.check_all_form_fields()

    def test_register_with_valid_data(self, browser):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys('Иван')
        register_page.last_name_input().send_keys('Иванов')
        register_page.email_input().send_keys('test777888890@gmail.com')
        register_page.password_input().send_keys('Passqwer12345')
        register_page.password_confirm_input().send_keys('Passqwer12345')
        register_page.register_button().click()
        register_page.check_confirm_email_page_title()

    @pytest.mark.parametrize('name', ('Й', 'Й'*31))
    def test_register_user_with_wrong_name(self, browser, name):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys(name)
        register_page.last_name_input().click()
        register_page.check_error_message('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

    @pytest.mark.parametrize('name', ('ЙЙЙ', 'Й' * 30))
    def test_register_user_with_correct_name(self, browser, name):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys(name)
        register_page.last_name_input().click()
        register_page.error_message_is_hidden()

    @pytest.mark.parametrize('name', ('Й', 'Й' * 31))
    def test_register_user_with_wrong_last_name(self, browser, name):
        register_page = self.register_page(browser)
        register_page.last_name_input().send_keys(name)
        register_page.name_input().click()
        register_page.check_error_message('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

    @pytest.mark.parametrize('name', ('ЙЙЙ', 'Й' * 30))
    def test_register_user_with_correct_last_name(self, browser, name):
        register_page = self.register_page(browser)
        register_page.last_name_input().send_keys(name)
        register_page.name_input().click()
        register_page.error_message_is_hidden()

    @pytest.mark.parametrize('email', ('@gmail.com', 'test.gmail.com', 'test@'))
    def test_register_user_with_wrong_email(self, browser, email):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys('Иван')
        register_page.last_name_input().send_keys('Иванов')
        register_page.email_input().send_keys(email)
        register_page.password_input().click()
        register_page.check_error_message('Введите телефон в формате +7ХХХХХХХХХХ '
                                          'или +375XXXXXXXXX, или email в формате example@email.ru')

    @pytest.mark.parametrize('password, error_msg', wrong_password)
    def test_register_user_with_wrong_password(self, browser, password, error_msg):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys('Иван')
        register_page.last_name_input().send_keys('Иванов')
        register_page.email_input().send_keys('test123456789@gmail.com')
        register_page.password_input().send_keys(password)
        register_page.password_confirm_input().click()
        register_page.check_error_message(error_msg)

    def test_register_user_with_wrong_confirm_password(self, browser):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys('Иван')
        register_page.last_name_input().send_keys('Иванов')
        register_page.email_input().send_keys('test123456789@gmail.com')
        register_page.password_input().send_keys('Qazdfghn231')
        register_page.password_confirm_input().send_keys('Qazdfghn2355656')
        register_page.register_button().click()
        register_page.check_error_message('Пароли не совпадают')

    def test_register_user_with_not_filled_fields(self, browser):
        register_page = self.register_page(browser)
        register_page.register_button().click()
        register_page.check_error_messages_for_all_fields()

    def test_check_default_region(self, browser):
        register_page = self.register_page(browser)
        register_page.check_default_region()

    @pytest.mark.parametrize('phone', ('‘961123111’', '96112311112'))
    def test_register_user_with_wrong_phone(self, browser, phone):
        register_page = self.register_page(browser)
        register_page.name_input().send_keys('Иван')
        register_page.last_name_input().send_keys('Иванов')
        register_page.email_input().send_keys(phone)
        register_page.password_input().click()
        register_page.check_error_message('Введите телефон в формате +7ХХХХХХХХХХ '
                                          'или +375XXXXXXXXX, или email в формате example@email.ru')
