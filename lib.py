from pathlib import Path
import os
import ctypes

# Return a dict which contains all the settings
def read_settings():
	settings = {}

	try:
		file = open(str(Path.home()) + '/.lk', 'r')
	except FileNotFoundError:
		print("You haven't got a configuration file. Try reinstalling.")
		exit()
	for iterator, line in enumerate(file):
		line = line.split('#')[0].strip()
		if len(line) == 0:
			continue
		line = ''.join(line).replace(' ', '').split('=')
		try:
			settings[line[0]] = line[1]
		except IndexError:
			print("Check line", iterator, "of ~/.lk")
			
	return settings

# Create the file which is used to track the latest kernel downloaded
def create_lklocation():
	global settings
	open(settings['lklocation'], 'w')


# Return true if the program is running as admin
def is_admin():
	try:
 		is_admin = os.getuid() == 0
	except AttributeError:
 		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	return is_admin

# The dict which contains all the settings
settings = read_settings()