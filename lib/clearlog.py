# -*- coding: utf-8 -*-
'''
Created on 2016-1-15

@author: Administrator
'''

import os,re,datetime
from basemonitor import BaseMonitor,MonitorStatus
from log import loger
from adbdevice import AdbDevice
import time

script_dir = os.path.dirname(os.path.realpath(__file__))

class AndroidResMonitor(BaseMonitor):

    def __init__(self,appnamelist,Type,serialNumber=None):
        self.appnamelist = appnamelist
        self.device=AdbDevice(Type,serialNumber)
        if not self.device.adbRoot():
            loger.logError(u"无法获取root权限，不能获得进程的内存情况！")
        self.device.runRootShellCmd("chmod 777 /data/")
        self.PID=self.getPid()
        print 'pid =',self.PID
        self.uid = self.getUid()
        print 'uid =',self.uid
        #self.casename=""
        '''self.NameToPid={}
        for appname in appnamelist:
            self.NameToPid[appname]=[]'''

    def getPid(self):#通过adb shell ps更新(获取)进程的pid值
        res=self.device.runCmd("shell ps")
        flag = False
        if not res:
            print 'ps faild'
            return False
        #print 'res =',res
        for res_item in res[1:-1]:
            print res_item.split()[-1]
            print self.appnamelist[0]
            print '---------------------'
            if  self.appnamelist[0]==res_item.split()[-1]:
                print 'finded'
                flag = True
                return res_item.split()[1]
        print 'flag =',flag
        if flag == False:
            print 'can not find pid'
                
    def getUid(self):#进程的uid值
        CMD="shell cat "#将所有需要cat的文件，一次都cat出
        CMD+="data/system/packages.list"
        res=self.device.runCmd(CMD)
        flag = False
        if not res:
            print 'ps faild'
            return False
        #print 'res =',res
        for res_item in res[1:-1]:
            print res_item.split()[-1]
            print '---------------------'
            if  self.appnamelist[0]==res_item.split()[0]:
                print 'finded'
                flag = True
                print res_item.split()[1]
                return res_item.split()[1]
        print 'flag =',flag
        if flag == False:
            print 'can not find uid'

    def get_networkTraffic(self):
        CMD="shell cat "#将所有需要cat的文件，一次都cat出
        CMD+="/proc/net/xt_qtaguid/stats"
            
        print 'CMD=',CMD
        res=self.device.runCmd(CMD)
        #print res
        list_rx = [] # 接收网络数据流量列表
        list_tx = [] # 发送网络数据流量列表
        try:
            for res_item in res[1:-1]:
                if res_item.split()[3] == self.uid:
                    rx_bytes = res_item.split()[5] # 接收网络数据流量
                    tx_bytes = res_item.split()[7] # 发送网络数据流量
                    list_rx.append(int(rx_bytes))
                    list_tx.append(int(tx_bytes))
            # print list_rx, sum(list_rx)
            floatTotalNetTraffic = (sum(list_rx) + sum(list_tx))/1024.0
            floatTotalNetTraffic = round(floatTotalNetTraffic,4)
            print 'net=',floatTotalNetTraffic,'kb'
            return floatTotalNetTraffic
        except:
                print "[ERROR]: cannot get the /proc/net/xt_qtaguid/stats, return 0.0"
                return 0.0

    def checkProcessPid(self,num,res):#检查进程id是否变换
        i=0 
        #print res
        #print "num: ",num
        #print "len appname:",len(self._appnames) 
        for appname in self._appnames:
            pidList=self.NameToPid[appname]
            for pid in pidList:
                #print res[i].split()[0],pid
                if res[i].split()[0]!=pid :#出现这个说明访问到了不存在的文件，说明进程已经停止运行，需要重新更新进程pid
                    #print "return False"
                    return False
                m=re.match(r'\((.*)\)',res[i].split()[1])#获取文件内容的第二个字段内容
                if m.group(1) not in  appname:#截取/proc/pid/stat文件的第二个字段，获得进程名称，看是否是以前的那个进程，不是就需要更新进程pid
                    return False
                i+=1
        return True
    

if __name__ == "__main__":
    from optparse import OptionParser
    usage = u"""usage: python AndroidResMonitor.py [options]
    Monitor the CPU ,Memory and the activity thread for the APP with pid or appname
    例子：
    指定进程名，监控多个进程
    python perf_command.py -n com.tencent.mobileqq -n com.tencent.mobileqq:MSF -o abc3.csv
    指定手机和进程名监控某个进程
    python perf_command.py -n com.tencent.mobileqq -o abc4.csv -s SH0AKPL02190
    """
    parser = OptionParser(usage)
    parser.add_option('-d', action="store_true", dest='device', help=u"连接真实的机器")
    parser.add_option('-e', action="store_true", dest='emulator', help=u"连接模拟器")
    parser.add_option('-p', '--pid', dest='pid', help=u"被监控的程序pid。可以使用多个-p代表监控多个进程。",action="append",metavar="Pids",default=[])
    parser.add_option('-s', '--serialNumber', dest='serialNumber', help=u"指定serialNumber连接设备", metavar="SerialNumber")
    parser.add_option('-o', '--output', dest="filename", help=u"指定数据输出文件(必须)", metavar="File",default=[])
    parser.add_option('-t', '--sample', dest='sampletime', help=u"取样间隔，默认为1秒", metavar="Sample")
    parser.add_option('-n', '--appname', dest='appname', help=u"被监控的程序名。可以使用多个-n代表监控多个进程", metavar="AppName", action="append",default=[])
    (options, args) = parser.parse_args()

    adbType=""
    serialNumber=""

    if (not options.appname) and not options.pid:
        print u"必须-n或者-p，指定被监控进程"
        parser.print_help()
        exit()
        
    elif (options.device and options.emulator):
        parser.print_help()
        exit()
    else:
        if options.device:
            adbType="-d"
        if options.emulator:
            adbType="-e"
        if options.serialNumber:
            adbType="-s"
            serialNumber=options.serialNumber
        if not options.sampletime:
            options.sampletime = float(0.5)
    print options.appname,options.pid
    monitor = AndroidResMonitor(options.appname,adbType,serialNumber)
    net1 = monitor.get_networkTraffic()
    print 'current net is',net1
    print 'begin...'
    flag = True
    str = raw_input("If finish you task,please input 'stop' in your keyboard: ")
    if str == 'stop':
        net2 = monitor.get_networkTraffic()
    net = net2- net1
    print 'networkTraffic is',net

    


