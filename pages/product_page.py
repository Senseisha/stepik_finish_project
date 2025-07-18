from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_book_name(self):
        WebDriverWait(self.browser, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.breadcrumb li.active")))
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



