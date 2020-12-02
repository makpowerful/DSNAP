import time
from pageObject.LoginPO import LoginPage
from utilities.readProperties import ReadConfig
from utilities.Customlogger import LogGen
from pageObject.CreateHHPO import CreateHHPO
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

    def test_CreateHH(self,setup):
        self.logger.info("**************** Test HH Creation ****************")
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
        if self.driver.title.startswith("HOU"):
            assert True
            self.logger.info("***** HH has been created successfully *****")
            self.driver.close()
        else:
            self.logger.info("**************** Test Login has failed ****************")
            self.driver.save_screenshot("C:\\Users\\mkalamshabaz\\PycharmProjects\\DSNAP\\Screenshots\\CreateHH.png")
            self.driver.close()
            assert False


