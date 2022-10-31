import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys

from utilites.logger import Logger


class Choosing_1_product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    menu = "//a[@href='/catalogue/']"
    link_about_1 = "//a[@href='/catalogue/kompyutery_i_periferiya-c243/']"
    link_about_2 = "//img[@class='drawCats__item__image']"
    link_about_3 = "//img[@class='drawCats__item__image']"
    show_all_models = "//a[@class='spoiledLst__showLink js__spoiledLst__showLink']"
    input_model = "//input[@data-filterid='producersFilterID']"
    show = "показать"
    xiaomi = "//label[@id='l46435b29b8bf4dd5d73b4a4fa25f3e50']"
    sort = "//select[@id='js__listingSort_ID']"
    laptop_1 = "Xiaomi Pro RedmiBook (XMA2009-DB)"
    compare = "Сравнить"
    apple = "//*[@id='l2a409a83fa51c7453545eb0e379d7926']/span[3]"
    laptop_2 = 'Apple MacBook Air 13,6"/2022/8-core Apple M2 chip 8-core GPU/8GB/256GB SSD, A2681, MLXY3LL/A Silver'

        # Getters

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about_1)))

    def get_link_about_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about_2)))

    def get_link_about_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about_3)))

    def get_show_all_models(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_models)))

    def get_input_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_model)))

    def get_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi)))

    def get_show(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.show)))

    def get_sort(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort)))

    def get_laptop_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.laptop_1)))

    def get_compare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.compare)))

    def get_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple)))

    def get_show(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, self.show)))

    def get_sort(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort)))

    def get_laptop_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.laptop_2)))


        # Actions

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_link_about_1(self):
        self.get_link_about_1().click()
        print("Click link about 1")

    def click_link_about_2(self):
        self.get_link_about_2().click()
        print("Click link about 2")

    def click_link_about_3(self):
        self.get_link_about_3().click()
        print("Click link about 3")

    def click_show_all_models_1(self):
        self.get_show_all_models().click()
        self.get_input_model().send_keys("xi")
        self.get_xiaomi().click()
        self.get_show().click()
        print("Click show all models")

    def click_sort_1(self):
        self.get_sort().click()
        self.get_sort().send_keys(Keys.DOWN)
        self.get_sort().send_keys(Keys.RETURN)
        print("Click sort")

    def click_laptop_1(self):
        self.get_laptop_1().click()
        print("Click laptop 1")

    def click_compare_1(self):
        self.get_compare().click()
        print("Click compare 1")

    def click_show_all_models_2(self):
        self.get_show_all_models().click()
        self.get_input_model().send_keys("xi")
        self.get_xiaomi().click()
        self.get_input_model().clear()
        self.get_input_model().send_keys("ap")
        self.get_apple().click()
        self.get_show().click()
        print("Click show all models")

    def click_sort_2(self):
        self.get_sort().click()
        self.get_sort().send_keys(Keys.DOWN)
        self.get_sort().send_keys(Keys.RETURN)
        print("Click sort")

    def click_laptop_2(self):
        self.get_laptop_2().click()
        print("Click laptop 2")

    def click_compare_2(self):
        self.get_compare().click()
        print("Click compare 2")

        """Methods"""

    def select_menu_about(self):

        Logger.add_start_step(method='select_menu_about')
        self.get_current_url()
        self.click_menu()
        self.click_link_about_1()
        self.click_link_about_2()
        self.click_link_about_3()
        Logger.add_end_step(url=self.driver.current_url, method='select_menu_about')

    def select_models_1(self):
        self.get_current_url()
        self.click_show_all_models_1()

    def select_sort_1(self):
        self.get_current_url()
        self.click_sort_1()

    def add_compare_1(self):
        self.get_current_url()
        self.click_laptop_1()
        self.click_compare_1()
        time.sleep(5)
        self.driver.back()

    def select_models_2(self):
        self.get_current_url()
        self.click_show_all_models_2()

    def select_sort_2(self):
        self.get_current_url()
        self.click_sort_2()

    def add_compare_2(self):
        self.get_current_url()
        self.click_laptop_2()
        self.click_compare_2()
