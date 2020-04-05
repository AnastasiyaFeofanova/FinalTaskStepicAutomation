from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color")

class AddToBasketLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner ")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner  p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
