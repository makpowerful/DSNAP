import time
from pageObject.LoginPO import LoginPage
from utilities.readProperties import ReadConfig
from utilities.Customlogger import LogGen


class Test_Login():
    url = ReadConfig.getApplicationurl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    Sdis = ReadConfig.getDisaster()
    SdisS = ReadConfig.getDisasterSite()
    logger = LogGen.loggen()

    def test_login(self, setup):

        self.logger.info("**************** Test Login ****************")
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
        self.lp.SelectDis(self.Sdis)
        time.sleep(2)
        self.lp.SelectDisSite(self.SdisS)
        time.sleep(2)
        self.lp.ClickGoto()
        time.sleep(2)
        self.lp.ClickAccept()
        time.sleep(10)
        if self.driver.title == 'Search Household | Salesforce':
            assert True
            self.logger.info("**************** Test Login has passed ****************")
            self.driver.close()
        else:
            self.logger.info("**************** Test Login has failed ****************")
            self.driver.save_screenshot("C:\\Users\\mkalamshabaz\\PycharmProjects\\DSNAP\\Screenshots\\Login.png")
            self.driver.close()
            assert False