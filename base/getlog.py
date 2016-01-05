# -*- coding: utf-8 -*-
# #!/usr/bin/env python
__author__ = 'Administrator'

import sys,os,time
import re

class getAppLog():
    '''  定义基类  :
                        判断andriod_home是否存在，继而判断adb命令是否存在
                        判断device是否在线，如果在线，获取devices信息
                        判断adb logcat是否可用
                        清空缓存日志
                        调用adb logcat捕获日志，并重定向到指定文件
                        如果日志文件超过20M，备份原日志文件
    '''

    def def_log_file(self,log_name=None):
        ''' 定义 日志文件   '''
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        log_name = 'test_logcat.txt' if log_name == None else log_name
        file_path = PATH(log_name)
        return file_path

    def envCheck(self):
        '''  校验 andriod sdk '''
        if "ANDROID_HOME" in os.environ:
            rootDir = os.path.join(os.environ["ANDROID_HOME"], "platform-tools")
            for path, subdir, files in os.walk(rootDir):
                if "adb.exe" in files:
                    return os.path.join(path, "adb.exe")
                else:
                    print '\nadb.exe does not exist!\n',
                    time.sleep(3)
        else:
            print "\nANDROID_HOME not exist! Please setup andriod SDK and set the environment variable ANDROID_HOME. \n",
            time.sleep(3)



    def get_device_id(self):
        '''  获取 deviceId，并作容错校验       '''
        #尝试停止、启动adb-server，方便调用adb获取信息
        os.popen('adb kill-server')
        time.sleep(3)
        os.popen('adb start-server')
        time.sleep(5)
        out = os.popen("adb devices").read()

        if out == '':
            print '\n[ERROR]  Terminal device has a problem, the program exits, replace the terminal equipment!\n'
            time.sleep(3)
            exit()
        elif out.startswith('error'):
            print '\n[ERROR]  Get devices error,program exits!\n'
            time.sleep(3)
            exit()
        elif out.split('\n')[1].strip().endswith('unauthorized') and str(out).count('device') == 1:
            print '\n[ERROR]  Device unauthorized,program exits!\n'
            time.sleep(3)
            exit()
        elif out.split('\n')[0].strip().endswith('attached') and str(out).count('device') == 1 and len(out.split('\n')) <= 3:
            print '\n[ERROR]  Not get list of devices,program exits!\n'
            time.sleep(3)
            exit()
        else:
            deviceId = out.split('\n')[1].split('\t')[0]
            return deviceId

    def check_log_is_enable(self):
        ''' 校验手机设备是否支持logcat命令   '''
        log_cat = os.popen("adb logcat -g 20").read()

        match = re.search(r'''Unable to open log device '/dev/log/main': No such file or directory''',log_cat)
        if match:
            print '\n[ERROR]  ' + log_cat + ' \n'
            time.sleep(3)
            sys.exit()

    def get_log_to_file(self,deviceid,file_path):
        ''' 调用logcat获取日志到文件
            adb -s deviceid logcat -c （清除LOGCAT的缓存）
            adb -d -s deviceid logcat *:W >test_logcat.txt
        '''

        if deviceid != '':
            clear_buffer = 'adb -s '+ deviceid  +' logcat -c '
            get_log = 'adb -d -s ' +  deviceid + ' logcat -v time -s *:W >>' + file_path

            if ' ' in file_path:
                print '\n ' + file_path + ': The path contains spaces,program exits!\n'
                time.sleep(3)
                sys.exit()

            #执行具体的命令
            os.system(clear_buffer)
            time.sleep(1)
            os.system(get_log)
        else:
            print '\ndeviceid not exist!\n'
            time.sleep(3)
            sys.exit()

    def log_file_size(self,file_path):
        ''' 如果log文件过大，备份并重新启用一个日志进行记录   '''
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)

            file_name = file_path.split("/")[-1].split('.')[0]
            file_Suffix =file_path.split("/")[-1].split('.')[-1]

            timeStamp =  time.strftime('%Y_%m_%d_%H_%M_%S')
            new_name = file_name+'_'+ timeStamp + file_Suffix
            if file_size >= 20971520:
                os.rename(file_path, new_name)



if __name__ == '__main__':
    print '-' * 75

    log = getAppLog()

    log_file = log.def_log_file()

    log.log_file_size(log_file)

    log.envCheck()

    device_id = log.get_device_id()

    log.check_log_is_enable()

    log.get_log_to_file(device_id,log_file)