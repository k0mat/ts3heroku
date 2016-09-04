import subprocess

def main():
	running = True
	command = 'ts3/ts3server_minimal_runscript.sh'
	while running:
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		process.wait()
		print process.returncode

if __name__ == '__main__':
	main()