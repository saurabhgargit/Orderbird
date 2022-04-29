
from base.BasePage import BasePage
import utilities.CustomLogger as cl


class AppLaunchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators values in App Launch page

    _echoBoxBtn = "Echo Box"
    _loginScreenBtn = "Login Screen"
    _listDemoBtn = "List Demo"
       # _loginPageTitle = "Login"

    def clickEchoBoxBtn(self):
        self.waitForElement(self._echoBoxBtn,"id")
        self.clickElement(self._echoBoxBtn,"id")
        cl.allureLogs("Clicked on Echo box menu")

    def clickLoginScreenBtn(self):
        self.clickElement(self._loginScreenBtn,"id")
        cl.allureLogs("Clicked on Login menu")

    def clickListDemoBtn(self):
        self.clickElement(self._listDemoBtn,"id")
        cl.allureLogs("Clicked on List Demo menu")
