from utilities.Customlogger import LogGen
from utilities.readProperties import ReadConfig

logger = LogGen.getloggen()
username = ReadConfig.getUsername()
logger.info('This is a sample message')
a = 1
print(username)
print(a)