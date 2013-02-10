#!/usr/bin/env python

import subprocess
from subprocess import PIPE, STDOUT
import re

def execute_commands(command_list, log_file):
	for command in command_list:
		print 'Executing:' + command
		system_execute = subprocess.Popen(command, stdin =PIPE, stderr=STDOUT, stdout=PIPE, shell=True)
		system_response = ""
		while True:
			line = system_execute.stdout.readline()
			if line != '':
				print line
				system_response += line + "\n"
			else:
				break

		log_file.write(system_response)
		log_file.write('\n')

#===============================================================================

git_commands = [
	'git init --bare /opt/git/app.git',
	'cp post-receive /opt/git/app.git/hooks',
	'mkdir /var/www',
	'cd /var/www && git clone /opt/git/app.git']

static_commands = [
	'yes | sudo apt-get install nginx',
	'sudo rm /etc/nginx/sites-enabled/*',
	'sudo cp static_nginx /etc/nginx/sites-enabled',
	'sudo service nginx start']

log_file = open('log.txt', 'w+')

execute_commands(git_commands, log_file)
execute_commands(static_commands, log_file)

print """System Installed!:
Git URL: username@<server_host>:/opt/git/app.git"""

log_file.write('Log file for installation\n')

log_file.close()