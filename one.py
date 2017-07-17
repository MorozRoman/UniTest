import unittest
import webium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Finds
import time

# Webium
class MainPage(BasePage):
    services = Finds(by=By.CLASS_NAME, value='popular-item')

    def __init__(self):
        super(MainPage, self).__init__(url="https://www.mos.ru/")


class one_mos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        webium.driver._driver_instance = self.driver
        driver = self.driver
        driver.maximize_window()

    def test_serach(self):

        main_page = MainPage()
        main_page.open()
        time.sleep(1)
        self.assertEqual(len(main_page.services), 10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

# UnitTest
# class one_mos(unittest.TestCase):
# 
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#     def test_popular(self):
#         driver = self.driver
#         driver.get("http://www.mos.ru")
#         self.assertEqual(len(driver.find_elements_by_class_name('catalog-services-popular__item')), 10)
#         time.sleep(5)
#     def tearDown(self):
#         self.driver.close()
# if __name__ == "__main__":
#     unittest.main()
