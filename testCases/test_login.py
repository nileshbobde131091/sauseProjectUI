import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser()
    lockedUser = ReadConfig.getLockedUser()
    password = ReadConfig.getPassword()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Swag Labs":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_wrongUser(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setLockedUserName(self.lockedUser)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        try:
            assert (error_message == "Epic sadface: Sorry, this user has been locked out.")
            self.driver.close()
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            raise (Exception("Additional info. %s" % e))
            self.driver.close()



