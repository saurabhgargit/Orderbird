import unittest

import pytest

from pages.AppLaunchPage import AppLaunchPage
from pages.ListDemoPage import ListDemoPage
import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass")
class ListDemoTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ap = AppLaunchPage(self.driver)
        self.ld = ListDemoPage(self.driver)

    @pytest.mark.order(1)
    def test_openListDemoPage(self):
        cl.allureLogs("App launched")
        self.ap.clickListDemoBtn()
        self.ld.verifyListDemoPage()

    @pytest.mark.order(2)
    def test_learnMoreAboutCirrus(self):
        exptectedCirrusSelectionMsg = "Your Cloud Selection\nCongratulations! You expressed interest in the Cirrus cloud"
        self.ld.clickCirrusButton()
        actualCirrusSelectionMsg = self.ld.verifyAlertMsgForCirrusInterest()
        assert actualCirrusSelectionMsg == exptectedCirrusSelectionMsg
        self.ld.clickOnCustomAlertOption("Learn more about Cirrus")
        actualCirrusLearnMoreMsg = self.ld.verifyAlertMsgForLearnMore()
        exptectedCirrusLearnMoreMsg = "Cirrus\nThis is a high-level cirriform mostly non-convective cloud"
        assert exptectedCirrusLearnMoreMsg == actualCirrusLearnMoreMsg
        self.ld.acceptAlert()

    @pytest.mark.order(3)
    def test_learnMoreAboutFog(self):
        exptectedFogSelectionMsg = "Your Cloud Selection\nCongratulations! You expressed interest in the Fog cloud"
        self.ld.clickFogButton()
        actualFogSelectionMsg = self.ld.verifyAlertMsgForCirrusInterest()
        assert actualFogSelectionMsg == exptectedFogSelectionMsg
        self.ld.clickOnCustomAlertOption("Learn more about Fog")
        actualFogLearnMoreMsg = self.ld.verifyAlertMsgForLearnMore()
        exptectedFogLearnMoreMsg = "Fog\nThis is a surface-level stratiform non-convective cloud"
        assert exptectedFogLearnMoreMsg == actualFogLearnMoreMsg
        self.ld.acceptAlert();

    @pytest.mark.order(4)
    def test_acceptCloudAlert(self):
        self.ld.clickStratocumulusButton()
        self.ld.clickOnCustomAlertOption("OK")
        self.ld.verifyListDemoPage()

    @pytest.mark.order(4)
    def test_dismissCloudAlert(self):
        self.ld.clickStratocumulusButton()
        self.ld.clickOnCustomAlertOption("Cancel")
        self.ld.verifyListDemoPage()
