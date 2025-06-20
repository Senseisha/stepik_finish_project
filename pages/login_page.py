from .base_page import BasePage
from .locators import LoginPageLocators
import time
# from mimesis import Person
# from mimesis.locales import Locale

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_url.click()
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "1579267345"
        form_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        form_email.send_keys(email)
        form_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        form_password1.send_keys(password)
        form_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        form_password2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    