# import allure
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    go_to_compare = "Перейти к сравнению"
    xiaomi = "Xiaomi Pro RedmiBook (XMA2009-DB)"
    selected_product = "//*[@id='goods_content']/div[1]/h1"
    buy = "//a[@data-handler='buy']"

    # Getters

    def get_go_to_compare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.go_to_compare)))

    def get_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.xiaomi)))

    def get_selected_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_product)))

    def get_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy)))

    # Actions

    def click_go_to_compare(self):
        self.get_go_to_compare().click()
        print("Click go to compare")

    def click_xiaomi(self):
        self.get_xiaomi().click()
        print("Click xiaomi")

    def click_buy(self):
        self.get_buy().click()
        print("Click plus")

    # Methods

    def select_product(self):

        Logger.add_start_step(method='select_product')
        self.get_current_url()
        self.click_go_to_compare()
        self.click_xiaomi()
        self.assert_word(self.get_selected_product(), 'Ноутбук Xiaomi Pro RedmiBook (XMA2009-DB)')
        time.sleep(5)
        self.click_buy()
        Logger.add_end_step(url=self.driver.current_url, method='select_product')

            



