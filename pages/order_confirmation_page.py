# import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


# from utilities.logger import Logger


class Order_confirmation_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    order_confirmation = "//*[@id='js__popup_addedToCart__cartLinkID']"
    oc_today = "//*[@id='main_area']/div[4]/div/form/div[2]/input"

    # Getters

    def get_order_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_confirmation)))

    def get_oc_today(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.oc_today)))

    # Actions

    def click_order_confirmation(self):
        self.get_order_confirmation().click()
        self.get_oc_today().click()
        print("Click order confirmation")


    # Methods

    def order_confirmations(self):

        Logger.add_start_step(method='order_confirmations')
        self.get_current_url()
        self.click_order_confirmation()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='order_confirmations')


