# -*- coding: utf-8 -*-
'''
Created on 2015-10-9

@author: Administrator
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


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        driver.quit()

    def test_bang(self):
        for i in range(0,20):
            sleep(5)
            mobiletext = loginPage.localtors['手机号']
            if i % 2 == 0:
                mobiletext.send_keys("13425156847")
            if i % 2 != 0:
                mobiletext.send_keys("13425152515")

            passwdtext = loginPage.localtors['密码']
            passwdtext.send_keys("123456")

            loginPage.localtors['登陆按钮'].click()
            sleep(10)
            mainpage = MainPage()
            mainpage.localtors['个人中心'].click()
            sleep(2)
            myinfo = MyInfoPage()
            myinfo.localtors['设置'].click()
            sleep(2)
            set =setPage()
            set.localtors['退出当前账号'].click()
            sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
    
    
    
    
    
    
#     print 'xxxxx'
#     suiteTest = unittest.TestSuite()
#     suiteTest.addTest(ContactsAndroidTests("test_bang"))
#     #确定生成报告的路径
#     filePath = "D:"
#     fp = file(filePath,'wb')
# 
#     #生成报告的Title,描述
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
#     runner.run(suiteTest)
#     print 'ccccc'