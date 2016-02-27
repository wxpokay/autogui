'''
Created on 2016-2-27

@author: Administrator
'''

from time import ctime,sleep
import threading
from base.logcat import getAndroidLogcat
#import HTMLTestRunner

class Threadlog(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        Androidlogcat = getAndroidLogcat()
        Androidlogcat.clearLogcat()
        filename = Androidlogcat.def_log_file()
        print  filename
        sleep(10)
        Androidlogcat.getLogcat(filename)
        sleep(1000)

class T2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #for i in range(100):
        print "I am subthread",ctime()

        
