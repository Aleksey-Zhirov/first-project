import time
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
# from pages.client_information_page import Client_information_page
# from pages.finish_button_page import Finish_page
from pages.login_page import Login_page
from pages.choosing_product import Choosing_1_product
from pages.order_confirmation_page import Order_confirmation_page


# from pages.payment_page import Payment_page


# @pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\\pythonSelenium\\chromedriver.exe', chrome_options=options)

    print("Start test 1")

    time.sleep(10)

    login = Login_page(driver)
    login.authorization()

    mp = Choosing_1_product(driver)
    mp.select_menu_about()
    mp.select_models_1()
    mp.select_sort_1()
    mp.add_compare_1()
    mp.select_models_2()
    mp.select_sort_2()
    mp.add_compare_2()

    cp = Cart_page(driver)
    cp.select_product()

    ocp = Order_confirmation_page(driver)
    ocp.order_confirmations()

    print("Finish test 1")
    time.sleep(10)
    driver.quit()



