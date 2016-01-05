# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import os
import unittest
from appium import webdriver
from time import sleep
from base.deviceAtrr import desired_caps
from base.deviceAtrr import driver

class loginPage():
    #滑动启动页
    sleep(5)
    def __init__(self):
        self.localtors = ({
            '手机号': driver.find_element_by_id('com.jhd.help:id/sEtUserName'),
            '密码': driver.find_element_by_id('com.jhd.help:id/sEtPassword'),
            '登陆按钮': driver.find_element_by_id('com.jhd.help:id/login_btn'),
            '注册按钮': driver.find_element_by_id('com.jhd.help:id/regist_text'), 
            })
    '''for i in range(3):
        driver.swipe(680, 200, 10, 680, 1500)
    driver.find_element_by_id('com.jhd.help:id/btn_instant_start').click()
    '''
    
class registPage():
    #滑动启动页
    def __init__(self):
        self.localtors = ({
            '手机号': driver.find_element_by_id('com.jhd.help:id/phone_number_edit'),
            '验证码': driver.find_element_by_id('com.jhd.help:id/verify_code'),
            '获取验证码': driver.find_element_by_id('com.jhd.help:id/get_number_code'),
            '密码': driver.find_element_by_id('com.jhd.help:id/password_editText'), 
            '注册': driver.find_element_by_id('com.jhd.help:id/next_btn'),                 
    })
    







