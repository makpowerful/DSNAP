import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\mkalamshabaz\\PycharmProjects\\DSNAP\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationurl():
        url = config.get('common values','url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common values','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common values','password')
        return password

    @staticmethod
    def getDisaster():
        Sdis = config.get('common values','Sdis')
        return Sdis

    @staticmethod
    def getDisasterSite():
        SdisS = config.get('common values','SdisS')
        return SdisS
