# -*- coding: utf-8 -*-
import os
import time
import subprocess
import thread
import sys
from log import *

class AdbDevice():
	def __init__(self,Type,serialNumber=None):
		self.adbType="adb "+Type+" "
		if  serialNumber:
			self.adbType=self.adbType+serialNumber+" "
# 		self.adbRoot()
# 		self.remount()
#		AdbDevice.startServer()
		
	def timer(self,process,TimeOut):
		num=0
		while process.poll()==None and num<TimeOut*10:
			num+=1
			time.sleep(0.1)
		if process.poll()==None:
			os.system("taskkill /T /F /PID %d"%process.pid)
			loger.logError(u"%d进程超时，被强行关闭！"%process.pid)
		thread.exit_thread()

	def runShellCmd(self,Cmd,TimeOut=3):
		return self.runCmd("shell \"%s\" "%Cmd, TimeOut)
	
	def runRootShellCmd(self,Cmd,TimeOut=3):
		res=self.runShellCmd("""su -c '%s'"""%Cmd, TimeOut)
		if res:
			for res_tiem in res:
				if "No such file or directory" in res_tiem:
					res=self.runShellCmd("""su -c %s"""%Cmd, TimeOut)
					break
		return res
	
	def runCmd(self,Cmd,TimeOut=3):
		process=subprocess.Popen(self.adbType+Cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		thread.start_new_thread(self.timer,(process,TimeOut))	
		#output,Error=process.communicate()
		res=process.stdout.read()
		process.wait()
		if process.poll() != 0:
			error=process.stderr.read()
			loger.logError(error)
			if "killing" in (res or error):
				loger.logError(u"请结束所有管理手的软件，尝试adb shell 是否能运行")
				sys.exit()
			if ("device not found" or "offline") in (res or error):
				loger.logError(u"设备未找到，或离线，请先保证adb shell能运行")
				sys.exit()
			if "more than one" in (res or error):
				loger.logError(u"多台设备连接电脑，请在调用时使用选项-s serialnumber，详细查看说明！")
				sys.exit()
			loger.logError(u"adb执行出错或超时，命令是：%s"%(self.adbType+Cmd))
			return None
		res=res.replace("\r\n","\n").splitlines()
		#print res
		if len(res)==0:
			return None
		return res

	def startNetcap(self,capfile):
		self.pushFile("tcpdump", "./data/tcpdump",4)
		self.runCmd("shell chmod 555 ./data/tcpdump")
		self.netcap=subprocess.Popen(self.adbType+'shell "./data/tcpdump  -l -X -n -s 0 -p -w ./data/%s >>/dev/null"'%capfile,shell=True)
	
	def stopNetcap(self):
		self.runCmd("shell pkill -2 tcpdump")
		time.sleep(1)

	def pushFile(self,src,dst,timeout=10):
		if self.runCmd("push "+src+" "+dst,timeout)!=None:
			loger.logError("传输文件失败！")

	def pullFile(self,src,dst):
		if self.runCmd("pull "+src+" "+dst)!=None:
			loger.logError("传输文件失败！")
		
	def adbRoot(self):
		if not self.runCmd("root"):
			loger.logError("ROOT失败！请按ReadMe教程获取adb root权限！")
			return False
		return True

	def logcat(self):
		if not self.runCmd("logcat -d"):
			loger.logError("获取日志失败！")
	
	def remount(self):
		if not self.runCmd("remount"):
			loger.logError("挂载磁盘失败！")

	def get_state(self):
		res=self.runCmd(self.adbType+"get-state")
		if not res:
			loger.logError("终端连接中断！")
			return
		return res.readline()[0]

	def wait_for_device(self,timeOut=120):
		if not self.runCmd(self.adbType+"wait-for-device",timeOut):
			loger.logWarning("adb等待超时")

	def install_package(self,path,TimeOut=30):
		if not self.runCmd("install %s"%path, TimeOut):
			loger.logWarning("安装文件不成功！")
			
	def start_activity(self,activityname):
		self.runCmd("shell am start %s"%activityname)
	
	def stop_package(self,package):
		self.runCmd("shell am force-stop %s"%package)
	
	def clear_package(self,package):
		self.runCmd("shell pm clear %s"%package)
		
	def input(self,string):
		self.runCmd("shell input text %s"%string)
		
	def press_keyevent(self,keyname):
		self.runCmd("shell input keyevent %s"%keyname)