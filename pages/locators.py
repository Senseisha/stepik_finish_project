from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class CatalogPage():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "ul.breadcrumb li.active")
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    # BOOK_NAME = (By.XPATH, "/li[@class='active']/text()")
    # BOOK_IN_BASKET = (By.XPATH, ".//[@id='message']//strong/text()")
    # BOOK_PRICE = (By.XPATH, "/p[contains(@class, 'product_main']/p[@class='price_color']/text()")
    # PRICE_IN_BASKET = (By.XPATH, "/div[@class='basket-mini']/strong/text()")