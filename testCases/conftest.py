import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options, executable_path='C:/Users/mkalamshabaz/Desktop/chromedriver.exe')
    return driver

def setupp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):  #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")


###Pytest HTML Report#########

#It is a hook for Adding Env Info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'DSNAP'
    config._metadata['Tester'] = 'Kalam'

#It is hook for delete/Modify Env info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Pulgins", None)






