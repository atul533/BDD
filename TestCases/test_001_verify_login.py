from Base.Init_Driver import Base
from Pages.LoginPage import LoginPage
import pytest
from Utilities.TestDataReader import data_generator


@pytest.mark.parametrize('cred', data_generator())
def test_verify_login(cred):

    driver = Base.init_driver()
    Base.launch_browser()
    login_page_obj = LoginPage(driver)
    login_page_obj.get_username().send_keys(cred[0])
    login_page_obj.get_password().send_keys(cred[1])
    login_page_obj.get_login_button().click()
    Base.close_browser()
