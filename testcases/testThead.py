'''
Created on 2016-2-27

@author: Administrator
'''
import threading
from time import ctime,sleep

class T(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #for i in range(100):
        print "I am subthread",ctime()
if __name__ == '__main__':
    t=T()
    t.setDaemon(True)
    t.start()
    for i in range(1000):
        print i,"I am main thread",ctime()
        
