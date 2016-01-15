# -*- coding: utf-8 -*-
'''
Created on 2016-1-15

@author: Administrator
'''

import os
import time

script_dir = os.path.dirname(os.path.realpath(__file__))
result = "F:\\workspace\\autogui\\logcat\\"

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
tdresult = result + day

class getAndroidLogcat:
    def def_log_file(self):
        ''' 定义 日志文件   '''
        print '定义日志文件'
        if os.path.exists(tdresult):
            filename = tdresult + "\\" + now + "_logcat.txt"
        else:
            os.mkdir(tdresult)
            filename = tdresult + "\\" + now + "_logcat.txt"
        return filename

    def clearLogcat(self):
        ''' 清除logcat  '''
        print '清除日志'
        
        os.popen("adb logcat -c")
        
                
    def getLogcat(self,file_path):
        ''' logcat取出  '''
        print '获取日志'
        cmd ='adb logcat -v time |findstr JHD >>' + file_path
        os.popen(cmd)


    

if __name__ == "__main__":
    getAndroidLogcat().clearLogcat()
    filename = getAndroidLogcat().def_log_file()
    print  filename
    time.sleep(10)
    getAndroidLogcat().getLogcat(filename)
    
    