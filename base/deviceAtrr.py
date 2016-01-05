# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {
    'platformName':'Android',
    'platformVersion':'4.4',
    'deviceName':'2a2d811',
    'app':PATH(
            'F:\Myappium\myapp\JHD_help_demoV1.5.8.4.apk_1.5.8.4.apk'),
    'appPackage':'com.jhd.help',
    'appActivity':'.module.welcome.SplashActivity',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)