import time
from pageObject.LoginPO import LoginPage
from pageObject.DC_CertPO import DC_CertPO
from pageObject.MPISearchPO import MPISearch
from pageObject.N_DSNAPCasePO import N_DSNAPCase
from pageObject.IntervieweePO import Interviewee
from utilities import XLUtils
from pageObject.CreateHOHPO import CreateHOH
from utilities.readProperties import ReadConfig
from utilities.Customlogger import LogGen
from pageObject.CreateHHPO import CreateHHPO
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

class Test_CreateHH():

    url = ReadConfig.getApplicationurl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    Sdis = ReadConfig.getDisaster()
    SdisS = ReadConfig.getDisasterSite()
    HH_url = ReadConfig.getApplicationHH_url()
    logger = LogGen.loggen()
    ResAddstr1 = ReadConfig.getResAddstr1()
    ResAddstr2 = ReadConfig.getResAddstr2()
    ResAddCity = ReadConfig.getResAddCity()
    ResAddZip = ReadConfig.getResAddZip()
    path="C:\\Users\\mkalamshabaz\\PycharmProjects\\DSNAP\\TestData\\DSNAP.xlsx"
    SSN = random.randint(100000000,888888899)
    GenderValue = 'Male'
    DocIDvalue = 'Passport'
    VRQ1 = ReadConfig.getVRQ1()
    VRQ2 = ReadConfig.getVRQ2()
    DIDR = ReadConfig.getDIDR()
    Exp = ReadConfig.getExp()

    def test_CreateHH(self,setup):
        self.logger.info("**************** Test HOH Creation ****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.EnterUsername(self.username)
        time.sleep(1)
        self.lp.EnterPassword(self.password)
        time.sleep(1)
        self.lp.ClickLogin()
        time.sleep(5)
        self.logger.info("***** Login has been successfully done. *****")
        self.lp.SelectDis(self.Sdis)
        time.sleep(2)
        self.lp.SelectDisSite(self.SdisS)
        time.sleep(2)
        self.lp.ClickGoto()
        time.sleep(2)
        self.lp.ClickAccept()
        time.sleep(3)
        self.logger.info("***** Selected disaster and disaster site successfully. *****")
        self.driver.get("https://la-dcfs--merge1.lightning.force.com/lightning/r/DSNAP_Case__c/a1Tr0000002BawiEAC/view")
        time.sleep(8)
        actions = ActionChains(setup)
        self.DC_Cert = DC_CertPO(self.driver)
        self.DC_Cert.Click_DID()
        time.sleep(3.5)
        self.DC_Cert.Sel_DIDQ1(self.DIDR)
        time.sleep(1)
        self.DC_Cert.Sel_DIDQ2(self.DIDR)
        time.sleep(1)
        self.DC_Cert.Sel_DIDQ3(self.DIDR)
        time.sleep(1)
        #actions.send_keys(Keys.PAGE_DOWN).perform()
        #time.sleep(2)
        self.DC_Cert.Sel_DIDQ4(self.DIDR)
        time.sleep(1)
        self.DC_Cert.Sel_DIDQ5(self.DIDR)
        time.sleep(1)
        self.DC_Cert.Sel_DIDQ6(self.DIDR)
        time.sleep(1)
        #actions.send_keys(Keys.PAGE_DOWN).perform()
        #time.sleep(2)
        self.DC_Cert.Ent_DIDQ7(self.DIDR)
        time.sleep(1)
        self.DC_Cert.Ent_DIDQ8(self.DIDR)
        time.sleep(1)
        self.DC_Cert.Ent_DIDQ9(self.Exp)
        time.sleep(1)
        actions.send_keys(Keys.TAB,Keys.ENTER).perform()
        time.sleep(4)
        #self.DC_Cert.Click_DIDSave()
        #time.sleep(3.5)
        #actions.send_keys(Keys.HOME).perform()
        #time.sleep(2)
        self.DC_Cert.Click_RR()
        time.sleep(4)
        self.DC_Cert.Click_RRQ1()
        time.sleep(2.5)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        self.DC_Cert.Click_RRQ2()
        time.sleep(2.5)
        self.DC_Cert.Click_RRQ2_Sign()
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        self.DC_Cert.Click_RRQ3()
        time.sleep(2)
        self.DC_Cert.Click_RRSave()
        time.sleep(4)
