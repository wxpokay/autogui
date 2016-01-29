# -*- coding: utf-8 -*-
'''
Created on 2016-1-23

@author: ritawu
'''
import os
import unittest
import time
#from appium import webdriver
from time import sleep
from testcases import test_login
from selenium.webdriver.support.expected_conditions import title_contains
#import HTMLTestRunner

#定义路径
script_dir = os.path.dirname(os.path.realpath(__file__))
result = "F:\\workspace\\autogui\\performance\\"

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

tdresult = result + day

#定义进程名字
pro = 'com.jhd.help'

def def_mem_file(self):   
    ''' 定义 日志文件   '''
    print '定义日志文件'
    if os.path.exists(tdresult):
        filename = tdresult + "\\" + now + "_mem.csv"
    else:
        os.mkdir(tdresult)
        filename = tdresult + "\\" + now + "_mem.csv"
        return filename

class MemInfo(unittest.TestCase):
    titleCmd = 'adb shell dumpsys meminfo com.jhd.help |findstr Pss>' + self.def_log_file()
    dataCmd = 'adb shell dumpsys meminfo com.jhd.help |findstr Total>>' + self.def_log_file()
    #cmd ='adb logcat -v time |findstr JHD >>' + 
    os.popen(titleCmd)
    os.popen(dataCmd)
    for i in range(50):
        test_login.LoginTests().test_login()
        test_login.LoginTests().test_logout()
            



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MemInfo)
    unittest.TextTestRunner(verbosity=2).run(suite)