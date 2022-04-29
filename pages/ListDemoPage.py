from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.BasePage import BasePage
import utilities.CustomLogger as cl


class ListDemoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in List Demo page
    _ListDemoPageTitle = "Check out these clouds"  # id
    _CirrusBtn = "Cirrus"  # id
    _FogBtn = "Fog"  # id
    _StratocumulusBtn = "Stratocumulus"  # id

    def verifyListDemoPage(self):
        element = self.isDisplayed(self._ListDemoPageTitle)
        assert element == True

    def clickCirrusButton(self):
        self.clickElement(self._CirrusBtn)
        cl.allureLogs("User has clicked on Cirrus cloud menu")

    def clickFogButton(self):
        self.clickElement(self._FogBtn)
        cl.allureLogs("User has clicked on Fog cloud menu")

    def clickStratocumulusButton(self):
        self.clickElement(self._StratocumulusBtn)
        cl.allureLogs("User has clicked on Stratocumulus cloud menu")

    def clickOnCustomAlertOption(self, text):
        buttons = self.driver.execute_script('mobile: alert', {'action': 'getButtons'})
        for i in buttons:
            if text == i:
                break
        alertArgs = {'action': 'accept', 'buttonLabel': i}
        self.driver.execute_script('mobile: alert', alertArgs)
        cl.allureLogs("User has clicked on "+text + "alert option")

    def verifyAlertMsgForCirrusInterest(self) -> str:
        alert = self.driver.switch_to.alert
        return alert.text

    def verifyAlertMsgForLearnMore(self) -> str:
        WebDriverWait(self.driver, 5).until (EC.alert_is_present())
        return self.driver.switch_to.alert.text

