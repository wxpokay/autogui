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

    
class MyMsgPage(object):
    #滑动启动页
    def __init__(self):
        sleep(5)
        self.localtors = ({
            '聊天窗口': driver.find_elements_by_class_name("android.widget.TextView"),                   
    })
        
class ChatPage(object):
    #滑动启动页
    def __init__(self):
        sleep(5)
        self.localtors = ({
            '输入框': driver.find_element_by_id('com.jhd.help:id/et_sendmessage'),
            '发送': driver.find_element_by_id('com.jhd.help:id/btn_send'),
            '文本消息': driver.find_elements_by_id('com.jhd.help:id/tv_chatcontent'),
            
                              
    })
