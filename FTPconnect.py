import ftplib
from threading import Thread
class ConnectionError(Exception):
		pass
class Connector:

		def __init__(self, config:dict):
				self.configuration = config['entry_config']
				self.Files = config['Files']
				
		def connect(self):
				self.ftp = ftplib.FTP(self.configuration['host'])
				self.conn_result = self.ftp.login(self.configuration['username'], \
												  self.configuration['password'])
				# 230 - Login successful. If it is not, raise Exception
				print(self.conn_result)
				if(self.conn_result[0:3] != '230'): 
						raise ConnectionError(result)
				return self.ftp
				

class  CopyThread(Thread):
		
		def __init__(self, config:dict, fid):
				self.Files = config['Files']
				self.fid = fid
				self.ftp = ftplib.FTP(config['entry_config']['host'])
				self.conn_result = self.ftp.login(config['entry_config']['username'], \
												  config['entry_config']['password'])
				Thread.__init__(self)

		def copy(self, FILE):
			with open(self.Files[FILE]['path'], 'rb') as binfile:
				self.ftp.storbinary('STOR ' + self.Files[FILE]['transfer_path'] , binfile, 1024)
			self.ftp.quit()	
		
		def run(self):
				self.copy(self.fid)           
		

