# -*- coding: utf-8 -*-

'''
Created on 2016-3-7

@author: Administrator
'''

import os
import time
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))
print script_dir
result = "F:\\workspace\\autogui\\meminfo\\"

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
tdresult = result + day

class getAndroidMem:
    def def_file(self):
        ''' 定义 存放内存数据的文件   '''
        print '定义 存放内存数据的文件 '
        if os.path.exists(tdresult):
            filename = tdresult + "\\" + now + "_mem.csv"
            
            
        else:
            os.mkdir(tdresult)
            filename = tdresult + "\\" + now + "_mem.csv"
        if(os.path.exists(filename)):
            print "已经存在了"
        else:
            print "不存在"
        return filename

    def getMemDump(self,file_path):
        ''' 获取操作的dump文件 '''
        print '获取操作的dump文件'
        
        subprocess.Popen('adb shell am dumpheap com.jhd.help>' +file_path)
        
                
    def getMemPic(self,file_path):
        ''' 获取内存趋势图  '''
        print '获取内存趋势图 '
        #f = open(file_path, 'w')
        cmd1 = 'adb shell dumpsys meminfo com.jhd.help |findstr Pss>>' + file_path
        #cmd1 = 'adb shell logcat -v time |findstr jhd >>' + file_path
        print cmd1
        subprocess.Popen(cmd1,shell=True)
        
        cmd2 = 'adb shell dumpsys meminfo com.jhd.help |findstr Total>>' + file_path
        
        subprocess.Popen(cmd2,shell=True)
        cmd3 = 'adb shell dumpsys meminfo com.jhd.help |findstr TOTAL>>' + file_path
        while(True):
            subprocess.Popen(cmd3,shell=True)


       
    

if __name__ == "__main__":
    filename = getAndroidMem().def_file()
    #print filename
    print '开始获取趋势'
    getAndroidMem().getMemPic(filename)