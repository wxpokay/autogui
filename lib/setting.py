# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import os
import unittest
from appium import webdriver
from time import sleep
from base.deviceAtrr import desired_caps
from base.deviceAtrr import driver

    
class setPage(object):
    #滑动启动页
    def __init__(self):
        sleep(5)
        self.localtors = ({
            '退出当前账号': driver.find_element_by_id('com.jhd.help:id/quit_account_btn'),  
    })
        
    '''for i in range(3):
        driver.swipe(680, 200, 10, 680, 1500)
    driver.find_element_by_id('com.jhd.help:id/btn_instant_start').click()
    '''
    







