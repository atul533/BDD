from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Utilities import ConfigReader


class Base:

    @staticmethod
    def init_driver():
        global driver
        browser = ConfigReader.get_config_data('Browser_Details', 'browser')
        if browser == 'chrome':
            driver = Chrome()
        elif browser == 'firefox':
            driver = Firefox()
        return driver

    @staticmethod
    def launch_browser():
        driver.get(ConfigReader.get_config_data('Browser_Details', 'URL'))
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.delete_all_cookies()

    @staticmethod
    def close_browser():
        driver.close()
