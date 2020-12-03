import time
from pageObject.LoginPO import LoginPage
from pageObject.MPISearchPO import MPISearch
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
        self.driver.get(self.HH_url)
        time.sleep(8)
        self.logger.info("***** Creation of HH *****")
        self.CHH = CreateHHPO(self.driver) # Creation of HH
        self.CHH.Click_New()
        time.sleep(5)
        self.CHH.Click_IsHomless()
        time.sleep(1)
        self.CHH.Click_IsHomless_N()
        time.sleep(1)
        self.CHH.Enter_ResAdd_Str1(self.ResAddstr1)
        time.sleep(1)
        self.CHH.Enter_ResAdd_Str2(self.ResAddstr2)
        time.sleep(1)
        self.CHH.Enter_ResAdd_City(self.ResAddCity)
        time.sleep(1)
        self.CHH.Enter_ResAdd_ZipC(self.ResAddZip)
        time.sleep(1)
        actions = ActionChains(setup)
        for _ in range(1):
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)
        self.CHH.Click_POO()
        time.sleep(1)
        self.CHH.Click_POO_Acadia()
        time.sleep(1)
        self.CHH.Click_MailAdd_Same()
        time.sleep(1)
        self.CHH.Click_MailAdd_Same_Y()
        self.CHH.Click_MailAdd_Str2()
        time.sleep(1)
        for _ in range(1):
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)
        self.CHH.Click_Rec_SNAP()
        time.sleep(1)
        self.CHH.Click_Rec_SNAP_N()
        time.sleep(1)
        self.CHH.Click_Mem_DCFS()
        time.sleep(1)
        self.CHH.Click_Mem_DCFS_N()
        self.CHH.Click_SNAPState()
        for _ in range(1):
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)
        self.CHH.Click_AuthRep()
        time.sleep(1)
        self.CHH.Click_AuthRep_N()
        time.sleep(1)
        self.CHH.Click_Save()
        time.sleep(5)
        self.logger.info("***** HH has been created successfully *****")
        self.logger.info("***** Creation of HH *****")
        self.CHOH = CreateHOH(self.driver)
        self.CHOH.ClickNewHHMem()
        time.sleep(5)

        self.rows=XLUtils.getRowCount(self.path,'HOH details')
        for r in range(2,self.rows+1):
            self.FN=XLUtils.readData(self.path,'HOH details',r,1)
            self.LN = XLUtils.readData(self.path, 'HOH details', r, 2)
            self.DOB = XLUtils.readData(self.path, 'HOH details', r, 3)

        self.CHOH.EnterFN(self.FN)
        time.sleep(1.5)
        self.CHOH.EnterLN(self.LN)
        time.sleep(1)
        self.CHOH.EnterDOB(self.DOB)
        time.sleep(1)
        self.CHOH.SelectGender(self.GenderValue)
        time.sleep(1)
        self.CHOH.EnterSSN(self.SSN)
        time.sleep(1)
        self.CHOH.Click_Save()
        time.sleep(3)
        self.logger.info ("***** HOH has been added successfully *****")
        self.logger.info("***** Performing MPI Search *****")
        self.MPIS = MPISearch(self.driver)
        self.MPIS.ClickHOH()
        time.sleep(4)
        self.MPIS.ClickLS()
        time.sleep(4)
        self.MPIS.ClickLS_Cancl()
        time.sleep(3)
        self.MPIS.ClickMPIS()
        time.sleep(4)
        self.MPIS.ClickMPIS_Cancl()
        time.sleep(3)
        self.TextMess = self.MPIS.ToastMess()
        if self.TextMess == "SSN is validated with provided SSN number.":
            assert True
            self.logger.info ("***** MPI search has been done successfully *****")
            self.driver.close()
        else:
            self.logger.info ("***** MPI search has not been done successfully *****")
            self.driver.save_screenshot("C:\\Users\\mkalamshabaz\\PycharmProjects\\DSNAP\\Screenshots\\MPISearch.png")
            self.driver.close()
            assert False


