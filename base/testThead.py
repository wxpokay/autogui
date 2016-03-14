'''
Created on 2016-2-27

@author: Administrator
'''

from time import ctime,sleep
import threading
from base.logcat import getAndroidLogcat
from base.getMeminfo import getAndroidMem
#import HTMLTestRunner

class Threadlog(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        Androidlogcat = getAndroidLogcat()
        Androidlogcat.clearLogcat()
        filename = Androidlogcat.def_log_file()
        print  filename
        Androidlogcat.getLogcat(filename)

class Threadmem(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        filename = getAndroidMem().def_file()
        #print filename
        print '开始获取趋势'
        getAndroidMem().getMemPic(filename)

class MemThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print "I am subthread",ctime()

        
