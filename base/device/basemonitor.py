# -*- coding: utf-8 -*-
'''
所有监控器的父类，负责维护csv文件，维护监控线程
'''

import csv
import os, sys
import time
import threading
import signal
from log import *

class MonitorStatus(object):
    '''监控器状态，如果有其他状态，可以在这里添加'''
    Running,Stoped = ("Running","Stoped")

class BaseMonitor(object):
    '''所有监控器的基类'''
    def __init__(self, tracefilename, appnames=[], pids=[]):
        self._pids = pids
        self._appnames = appnames
        if not self._pids and not appnames:
            raise Exception(u"请设置appnames或者pids")
        self._status = MonitorStatus.Stoped
        self._outfile = open(tracefilename, 'wb',200)
        self._writer = csv.writer(self._outfile)
        #signal.signal(signal.SIGINT, self.handler_killsign)
    
    @property
    def STATUS(self):
        return self._status
    
    def getInfo(self):
        '''@summary: 必须要集成此方法，并反馈list形式的数据'''
        raise Exception(u"请继承此方法，并返回list形式的数据")
    
    def _getInfoBySampleTime(self, sampletime):
        '''@summary: 按照取样时间间隔，获取数据，并保存在文件中'''
        while(True):
            time.sleep(sampletime)
            info = self.getInfo()
            if self._status is MonitorStatus.Stoped:
                loger.logDebug(u"停止获取数据 %s")
                break
            if not info:
                continue
            self._writer.writerow(info)
    
    def start(self, sampletime):
        '''@summary: 开始监控器'''
        if self._status is MonitorStatus.Running:
            loger.logWarning(u"请先调用stop方法再start %s")
            return

        self._status = MonitorStatus.Running
        self._monitorthread = threading.Thread(target=self._getInfoBySampleTime, args=(sampletime,))
        self._monitorthread.daemon=True
        self._monitorthread.start()
        
        while self._monitorthread.isAlive():
            try:
                pass
            except KeyboardInterrupt:
                self.stop()
                
        return
    
    def closefile(self):
        self._outfile.flush()
        self._outfile.close()     
    
    def stop(self):
        '''@summary: 停止监控器'''
        loger.logDebug(u"开始停止数据收集 %s")
        if self._status is not MonitorStatus.Running:
            return
        self._status = MonitorStatus.Stoped
        self._monitorthread.join(5)
        if self._monitorthread.isAlive():
            loger.logWarning(u'尝试取消监控线程失败 %s')
        self._outfile.flush()
        self._outfile.close()
    
    def getPid(self, procname):
        """@summary: 通过processname获取pid，若是多实例，只返回第一个实例"""
        raise Exception(u"请继承此方法，根据procname返回pid")
    
    def handler_killsign(self, n=0, e=0):
        print "receive kill signal"
        self.stop()
        sys.exit()
