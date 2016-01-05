# -*- coding: utf-8 -*-
'''
Created on 2015-12-21

@author: Administrator
'''

import os
import unittest
from appium import webdriver
from time import sleep
from base.deviceAtrr import desired_caps
from base.deviceAtrr import driver

    
class MainPage(object):
    #滑动启动页
    def __init__(self):
        sleep(5)
        self.localtors = ({
            '个人中心': driver.find_element_by_id('com.jhd.help:id/setting_image'),                   
    })
        
    '''for i in range(3):
        driver.swipe(680, 200, 10, 680, 1500)
    driver.find_element_by_id('com.jhd.help:id/btn_instant_start').click()
    '''
    







