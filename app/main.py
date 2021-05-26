# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import platform


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
desired_caps = {'platformName': 'Android',
                'platformVersion': '3.6.8',
                'deviceName': 'MEIZU_E3',     #设备名来自adb devices
                "appPackage": " com.meizu.flyme.flymebbs",
                "appActivity": ".ui.LoadingActivity",}
appium_server = 'http://localhost:4723/wd/hub'


class LearnAppiumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server, desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        text_view = self.driver.find_element_by_id("text_view")
        assert text_view.text == 'Hello World! Hello World!'  # 测试应该不通过

    def test_02(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        button = self.driver.find_element_by_id("button")
        button.click()

        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.ID, 'text_view')))
        text_view = self.driver.find_element_by_id("text_view")
        assert text_view.text == '3'  # 测试应该通过


if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
