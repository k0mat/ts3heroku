#!/usr/bin/python

import sys
import subprocess

def main(port):
	running = True
	command = 'ts3/ts3server_minimal_runscript.sh'
	args = 'default_voice_port=' + port
	while running:
		process = subprocess.Popen(command + ' ' + args, shell=True, stdout=subprocess.PIPE)
		process.wait()
		print process.returncode

if __name__ == '__main__':
	if !len(sys.argv) == 2:
		print 'Please specify port in command line'
		return
	main(sys.argv[1])
