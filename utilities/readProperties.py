import configparser
from selenium import webdriver
from testCases import conftest

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

    @staticmethod
    def getApplicationHH_url():
        HH_url = config.get('common values','HH_url')
        return HH_url

    @staticmethod
    def getResAddstr1():
        ResAddstr1 = config.get('common values','ResAddstr1')
        return ResAddstr1

    @staticmethod
    def getResAddstr2():
        ResAddstr2 = config.get('common values','ResAddstr2')
        return ResAddstr2

    @staticmethod
    def getResAddCity():
        ResAddCity = config.get('common values','ResAddCity')
        return ResAddCity

    @staticmethod
    def getResAddZip():
        ResAddZip = config.get('common values','ResAddZip')
        return ResAddZip

