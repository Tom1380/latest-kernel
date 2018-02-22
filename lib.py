from pathlib import Path
import os
import ctypes
import json
import re

# Return a json which will be used as a dict that contains all the settings
def read_config():
	try:
		config_file = open(str(Path.home()) + '/.lk', 'r')
	except FileNotFoundError:
		print("You haven't got a configuration file. Try reinstalling.")
		exit()
	config_str = config_file.read()
	config_str = re.sub(r'\\\n', '', config_str)
	config_str = re.sub(r'//.*\n', '\n', config_str)

	return json.loads(config_str)

# Create the file which is used to track the latest kernel downloaded
def create_lklocation():
	global config
	open(config['lklocation'], 'w')


# Return true if the program is running as admin
def is_admin():
	try:
 		is_admin = os.getuid() == 0
	except AttributeError:
 		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	return is_admin

# The dict which contains all the settings
config = read_config()