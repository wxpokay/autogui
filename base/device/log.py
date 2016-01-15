# -*- coding: utf-8 -*-
import os
import logging.config

def decorate(func):
	
	def encoded_judge(self,msg):
		if not isinstance(msg,unicode):
			try:
				msg=msg.decode("utf8")
			except UnicodeDecodeError:
				pass
		if isinstance(msg,unicode):
			msg=msg.encode('gbk')
		func(self,msg)
		
	return encoded_judge

class Log(object):
	def __init__(self,path=None,keys=None):
		if not path:
			logging.config.fileConfig(os.path.dirname(__file__) + "\\logging.conf")
		else :
			logging.config.fileConfig(path)
		if not keys:
			self._logger=logging.getLogger("Common")
		else :
			self._logger=logging.getLogger(keys)
	
	@decorate
	def logDebug(self,msg):
		self._logger.debug(msg)
	
	@decorate
	def logWarning(self,msg):
		self._logger.warning(msg)
	
	@decorate
	def logError(self,msg):
		self._logger.error(msg)
	
	@decorate
	def logInfo(self,msg):
		self._logger.info(msg)

loger=Log()

