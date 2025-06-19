from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        # assert basket_button
        basket_button.click()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET)
        assert book_name.text == book_in_basket.text

    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert book_price.text == price_in_basket.text
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared"



