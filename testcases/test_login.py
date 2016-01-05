# -*- coding: utf-8 -*-
'''
Created on 2015-12-21

@author: Administrator
登陆退出功能
'''

#import os
import unittest
#import time
#from appium import webdriver
from time import sleep
from base.deviceAtrr import driver
from lib.loginAndRegist import loginPage
from lib.setting import setPage
from lib.myinfo import MyInfoPage
from lib.mainpage import MainPage
#import HTMLTestRunner


class LoginTests(unittest.TestCase):
    def test_login(self):
        sleep(5)
        mobiletext = loginPage.localtors['手机号']
        mobiletext.send_keys("13425152515")

        passwdtext = loginPage.localtors['密码']
        passwdtext.send_keys("123456")

        loginPage.localtors['登陆按钮'].click()
        sleep(10)
    def test_logout(self):
        mainpage = MainPage()
        mainpage.localtors['个人中心'].click()
        sleep(2)
        myinfo = MyInfoPage()
        myinfo.localtors['设置'].click()
        sleep(2)
        setpage =setPage()
        setpage.localtors['退出当前账号'].click()
        sleep(2)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
        
