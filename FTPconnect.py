import ftplib
import time
class Connector:
# provides connection and the copy method

	def __init__(self, config:dict):
		self.configuration = config['entry_config']
		self.Files = config['Files']
		
	def connect(self):
		self.ftp = ftplib.FTP(self.configuration['host'])
		self.conn_result = self.ftp.login(self.configuration['username'], \
					     self.configuration['password'])
		return self.ftp
		
	def copy(self, id:int):
	# uploading file to the ftp server
	# id - file identificator from config.json
		for item in self.Files:
			if(item["id"]) == id:
				with open(item['path'], 'rb') as binfile:
					#wait 5 seconds to give access to user before 
					#the lock of control thread
					time.sleep(5)
					print('\nUploading started.File id:', id)
					self.ftp.storbinary('STOR ' + item['transfer_path'] , binfile, 1024)
					print('Uploading completed.File id:', id)
			
