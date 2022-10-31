from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Login_page(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    entrance = "//span[@class='ic__set ic__set__member']"
    user_name = "//input[@id='ajax_login_popup_email']"
    password = "//input[@id='ajax_login_popup_pass']"
    login_button = "//input[@name='submit']"

    # Getters

    def get_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entrance)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))



        # Actions

    def click_entrance(self):
        self.get_entrance().click()
        print("Click authorization")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

        # Methods

    def authorization(self):

        Logger.add_start_step(method='authorization')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_entrance()
        self.input_user_name("foxxxAPB@yandex.ru")
        self.input_password("12345")
        self.click_login_button()
        Logger.add_end_step(url=self.driver.current_url, method='authorization')