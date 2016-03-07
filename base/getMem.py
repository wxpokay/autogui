# -*- coding: utf-8 -*-

'''
Created on 2016-3-7

@author: Administrator
'''

import os
import time
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))
result = "F:\\workspace\\autogui\\mem\\"

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
tdresult = result + day

class getAndroidMem:
    def def_file(self):
        ''' 定义 日志文件   '''
        print '定义日志文件'
        if os.path.exists(tdresult):
            #filename1 = tdresult + "\\" + now + "_mem.txt"
            fielname2 = tdresult + "\\" + now + "_mem.txt"
        else:
            os.mkdir(tdresult)
            #filename1 = tdresult + "\\" + now + "_mem.csv"
            filename2 =tdresult + "\\" + now + "_mem.csv"
        return filename2

    def getMemDump(self,file_path):
        ''' 获取操作的dump文件 '''
        print '获取操作的dump文件'
        
        subprocess.Popen("adb shell am heapdump com.jhd.help"+file_path)
        
                
    def getMemPic(self,file_path):
        ''' 获取内存趋势图  '''
        print '获取内存趋势图 '
        cmd1 = 'adb shell dumpsys meminfo com.jhd.help |findstr Pss'>>+file_path
     
        subprocess.Popen(cmd1)
        cmd2 = 'adb shell dumpsys meminfo com.jhd.help |findstr Total'>>+file_path
        
        subprocess.Popen(cmd2)
        while(True):
            cmd2 = 'adb shell dumpsys meminfo com.jhd.help |findstr Total'>>+file_path
            subprocess.Popen(cmd2)


       
    

if __name__ == "__main__":
    filename = getAndroidMem().def_file()
   # getAndroidMem.getMemDump(filename)
    getAndroidMem.getMemPic(filename)
    