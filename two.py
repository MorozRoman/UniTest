import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webium import BasePage, Find
from selenium.webdriver.remote.webelement import WebElement
from webium.driver import get_driver

# Webiumm

class Elements(WebElement):
    lypa = Find(by=By.CLASS_NAME, value='mos-layout-icon-search_black')
    text_input = Find(by=By.CLASS_NAME, value='tt-input')

class ManePage(BasePage):
    search = Find(Elements, by=By.CLASS_NAME, value ='mos-search-form')

    def __init__(self):
        super(ManePage, self).__init__(url='http://www.mos.ru')

    def button(self):
        self.search.lypa.click()

    def get_result (self):
        self.search.lypa.click()
        return SearchResultPage()


class SearchResultPage(BasePage):
    widget = Find(by=By.CLASS_NAME, value="wdg-mayor")

if __name__ == '__main__':
    page = ManePage()
    page.open()
    page.button()
    page.search.text_input.send_keys(u"Собянин")
    result_page=page.get_result()
    print (result_page.is_element_present('widget'))
    get_driver().quit()
    unittest.main()


# Unittest
# class two_mos(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#     def test_serach(self):
#         driver = self.driver
#         driver.maximize_window()
#         driver.get("http://www.mos.ru")
#         driver.find_element_by_class_name('mos-layout-icon-search_black').click()
#         driver.find_element_by_class_name('tt-input').send_keys(u'Собянин')
#         driver.find_element_by_class_name('mos-layout-icon-search_black').click()
#         driver.implicitly_wait(10)
#         driver.find_element_by_class_name('wdg-mayor')
#         time.sleep(5)
#     def tearDown(self):
#         self.driver.close()
# if __name__ == "__main__":
#     unittest.main()
