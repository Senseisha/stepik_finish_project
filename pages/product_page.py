from .base_page import BasePage
from .locators import CatalogPage

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        basket_button = self.browser.find_element(*CatalogPage.BASKET_BUTTON)
        assert basket_button
        basket_button.click()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*CatalogPage.BOOK_NAME)
        book_in_basket = self.browser.find_element(*CatalogPage.BOOK_IN_BASKET)
        assert book_name.text == book_in_basket.text

    def should_be_book_price(self):
        book_price = self.browser.find_element(*CatalogPage.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*CatalogPage.PRICE_IN_BASKET)
        assert book_price.text == price_in_basket.text
        



