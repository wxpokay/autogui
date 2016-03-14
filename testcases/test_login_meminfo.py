# -*- coding: utf-8 -*-
'''
登陆退出功能
Created on 2015-12-21

@author: Administrator
登陆退出功能
'''


import unittest
from time import sleep
from base.deviceAtrr import driver
from lib.loginAndRegist import loginPage
from lib.setting import setPage
from lib.myinfo import MyInfoPage
from lib.mainpage import MainPage
from base.testThead import Threadmem
#import HTMLTestRunner


class LoginTests(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        driver.quit()
        
    def test_login(self):
        #启动页时间
        sleep(5)
        #滑过引导页
        for i in range(3):
            driver.swipe(680, 200, 10, 680, 1500)
        #点击引导页上的进入按钮
        driver.find_element_by_id('com.jhd.help:id/btn_instant_start').click()
        loginpage = loginPage()
        mobiletext = loginpage.localtors['手机号']
        mobiletext.send_keys("13425152515")

        passwdtext = loginpage.localtors['密码']
        passwdtext.send_keys("123456")

        loginpage.localtors['登陆按钮'].click()
        sleep(10)
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
    '''用子线程来获取logcat日志'''
    from base.testThead import Threadlog
    tLog=Threadlog()  
    tMem= Threadmem() 
    tLog.setDaemon(True)
    tLog.start()
    tMem.setDaemon(True)
    tMem.start()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
        
