from base.BasePage import BasePage

import utilities.CustomLogger as cl

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators value in Login page
    _loginField = "username"  # name
    _passwordField = "password"  # name
    _loginBtn = "(//XCUIElementTypeOther[@name=\"loginBtn\"])[2]"  # name
    _pageTitle = "Login"  # id

    def verifyLoginPage(self):
        element = self.isDisplayed(self._pageTitle, "id")
        assert element == True

    def enterEmail(self, text):
        self.sendText(text,self._loginField,"name")
        cl.allureLogs("User has entered email address")

    def enterPassword(self, password):
        self.sendText(password,self._passwordField,"name")
        cl.allureLogs("User has entered password")

    def clickLoginButton(self):
        self.clickElement(self._loginBtn,"xpath")
        cl.allureLogs("User has clicked on Login Button")
        self.screenShot("Login Screenshot")

    def acceptAlert(self):
        self.driver.switch_to.alert.accept()
