import unittest
import pytest
import utilities.CustomLogger as cl

from pages.AppLaunchPage import AppLaunchPage
from pages.EchoBoxPage import EchoBoxPage

log = cl.customLogger()


@pytest.mark.usefixtures("beforeClass")
class EchoBoxTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        log.info("launching App")
        self.ap = AppLaunchPage(self.driver)
        self.eb = EchoBoxPage(self.driver)

    @pytest.mark.order(2)
    def test_withOnlyOneCharacter(self):
        cl.allureLogs("User has entered inside echo box menu")
        self.eb.deleteText()
        self.eb.enterTextInMsgField("H")
        self.eb.clickSaveBtn()
        self.eb.verifyEchoBoxPage()

    @pytest.mark.order(1)
    def test_withValidData(self):
        self.ap.clickEchoBoxBtn()
        self.eb.enterTextInMsgField("Hello")
        self.eb.clickSaveBtn()
        self.eb.verifyEchoBoxPage()

    @pytest.mark.order(4)
    def test_withMaxLength(self):
        self.eb.deleteText()
        self.eb.enterTextInMsgField("Hey Champ, How are you doing today")
        self.eb.clickSaveBtn()
        self.eb.verifyEchoBoxPage()

    @pytest.mark.order(3)
    def test_withOnlySpace(self):
        self.eb.deleteText()
        self.eb.enterTextInMsgField(" ")
        self.eb.clickSaveBtn()
        self.eb.verifyEchoBoxPage()
