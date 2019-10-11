import ftplib
import json
from FTPconnect import Connector, CopyThread
from threading import Thread


# Opening config file
try:
	with open("config.json") as data_json:
		data = json.load(data_json)
except FileNotFoundError:
	print('config.json file is missing.')
	exit(1)
	
# Connecting to FTP server
conn = Connector(data)
try:
        conn.connect()
        print(conn.conn_result)
except ConnectionError:
        print('Connection faled: check login/pass ')
        exit(2)

#Options
def menu():
	Threads = []
	while(True):
		option = input()
		if(option=='q'):
		#exit the program
			
			for thread in Threads:
  				thread.join()
			try:
				conn.ftp.quit()
			except ConnectionResetError as err:
				print(err)
			break
		if(option[0:2] == 'cp'):
		#uploading the file. Example: cp 1
		        try:
		                File_id = int(option[3:])
		        except ValueError:
		        	print('File id is a number')
		        
		 
		        cpThread = CopyThread(data,File_id)
		        Threads.append(cpThread)
		        cpThread.start()

		if(option == 'ls'):
		#list directory contents
		        conn.ftp.retrlines('LIST')
		        
		if(option[0:2] == 'cd'):
		#change directory. Example: cd Hello
		        try:
		        	conn.ftp.cwd(option[3:])
		        except ftplib.error_perm:
		        	print('No such directory')

if __name__ == '__main__':
	menu()
