from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.NOT_PRODUCT), "Product in basket, but should not be"

    def should_be_message_basket_is_empty(self):
        message = self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY).text
        assert message.startswith("Ваша корзина пуста") or message.startswith("Your basket is empty")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," " probably unauthorised user"