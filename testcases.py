__author__ = 'Administrator'


import os
import unittest
import time
from appium import webdriver
from time import sleep
from base.deviceAtrr import driver
from lib.loginAndRegist import loginPage
import HTMLTestRunner
from testcases import test_contact


#suite = unittest.TestLoader().loadTestsFromTestCase(test_contact.ContactsAndroidTests)
#unittest.TextTestRunner(verbosity=2).run(suite)

suiteTest = unittest.TestSuite()
suiteTest.addTest(test_contact.ContactsAndroidTests("test_bang"))
print 'paopaopaopaopao'
#确定生成报告的路径
filePath = "F:\\Myappium"
fp = file(filePath,'wb')

#生成报告的Title,描述
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
runner.run(suiteTest)
print 'paopaopaoapo'
