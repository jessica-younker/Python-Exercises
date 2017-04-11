#read write append log file based on arguments we pass in
#data persistance	
#with statments are cool bc they automatically close the file
import sys
#datetime method from datetime module:
from datetime import datetime
from time import time

global file_name
global action

def read_log():
	"""Reads from the log file"""
	with open(file_name, 'r') as log_messages:
		print(log_messages.read())

def log(message):
	"""log a message to the log file"""
	"""Arguments: message--any string in command line after calling file"""
	#a appends message, w overwrites, r reads
	with open(file_name, 'a') as logger:
		timestamp = time()
		logger.write("{0}: {1}\n".format(
			datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
			str(message)
			))

if __name__ == '__main__':
    try: 
        file_name = sys.argv[1]
        action = sys.argv[2]
        if action == 'r':
                read_log()
        elif action == 'w' or action == 'a':
                log(" ".join(sys.argv[3:]), action)
                read_log()

    except IndexError:
        pass        