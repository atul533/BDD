from Base.Init_Driver import Base
import pytest


class LoginPage(Base):

    __username = "username"
    __password = "password"
    __login_button = "//button[text()='Log In']"

    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element_by_id(self.__username)

    def get_password(self):
        return self.driver.find_element_by_id(self.__password)

    def get_login_button(self):
        return self.driver.find_element_by_xpath(self.__login_button)
