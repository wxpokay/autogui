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
from lib.loginAndRegist import loginPage,registPage
from lib.setting import setPage
from lib.myinfo import MyInfoPage
from lib.mainpage import MainPage
#import HTMLTestRunner


class LoginTests(unittest.TestCase):
    def test_login(self):
        for i in range(3):
            driver.swipe(680, 200, 10, 680, 1500)
        driver.find_element_by_id('com.jhd.help:id/btn_instant_start').click()
        sleep(3)
        list = ('18507551002','18507551003','18507551004','18507551005','18507551006',
                '18507551007','18507551008','18507551009','18507551010','18507551011','18507551012','1850755100113','185075510014')
        for i in range(0,13):
            login = loginPage()
            login.localtors['注册按钮'].click()
            regist = registPage()
            regist.localtors['手机号'].send_keys(list[i])
            regist.localtors['获取验证码'].click()
            sleep(5)
            regist.localtors['验证码'].send_keys("123456")
            sleep(1)
            regist.localtors['密码'].send_keys("123456")
            regist.localtors['注册'].click()
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
        

