# -*- coding: utf-8 -*-
'''
Created on 2015-12-21

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
from lib.mymsgpage import MyMsgPage
from lib.mymsgpage import ChatPage
#import HTMLTestRunner


class SendMsg(unittest.TestCase):
    def test_sendmsg(self):
        sleep(5)
        mobiletext = loginPage.localtors['手机号']
        mobiletext.send_keys("13425152515")

        passwdtext = loginPage.localtors['密码']
        passwdtext.send_keys("123456")

        loginPage.localtors['登陆按钮'].click()
        sleep(5)
        mainpage = MainPage()
        mainpage.localtors['个人中心'].click()
        sleep(2)
        myinfo = MyInfoPage()
        myinfo.localtors['我的消息'].click()
        sleep(10)
        msgpage = MyMsgPage()
        for i in range(20):
            print msgpage.localtors['聊天窗口'][i].text
            if msgpage.localtors['聊天窗口'][i].text == 'bang6052':
                break  
        print '查找会话窗口结束啦！！'                  
        msgpage.localtors['聊天窗口'][i].click()
        sleep(2)
        chatpage = ChatPage()
        for i in range(200):
            sendtext = 10000000*(i+1)
            print sendtext
            chatpage.localtors['输入框'].send_keys(sendtext)
            sleep(3)
            chatpage.localtors['发送'].click()
            sleep(3)
        
        #for i in range(2):
            #print chatpage.localtors['文本消息'][i].text
        #self.assertEqual('哈哈哈', chatpage.localtors['文本消息'])
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SendMsg)
    unittest.TextTestRunner(verbosity=2).run(suite)
