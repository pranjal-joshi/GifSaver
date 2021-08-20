#!/usr/bin/python3

import sys
import subprocess as sp
import os
import glob
import random
import signal
import argparse as ap
from time import sleep
#from daemonize import Daemonize

# Constants
pidPath = '/tmp/GifSaver.pid'
DEBUG = False
if DEBUG:
	print("[+] GifSaver - Debug Enabled")
	print(f'My PID = {os.getpid()}')

def getArgs(args=None):
	parser = ap.ArgumentParser()
	parser.add_argument('-f', '--folder', help='Path to GIF Folder', required=True)
	parser.add_argument('-t', '--timeout', help='Idle Timeout to Start Screensaver', default=60, type=int)
	res = parser.parse_args()
	if DEBUG:
		print('Arguments:')
		print(f'Folder = {res.folder}')
		print(f'Timeout = {res.timeout}')
	return (res.folder, res.timeout)

def getFiles(path):
	filelist = glob.glob(path + "/*")
	if DEBUG:
		print(f'FileList = {filelist}')
	return filelist

def killDaemon(x, *args):
	print("SIGTERM - Killing GifSaver Daemon!")
	daemonPid = None
	with open(pidPath) as pidFile:
		daemonPid = int(pidFile.read())
	if daemonPid is not None:
		os.kill(daemonPid, signal.SIGTERM)

# Screensaver Method
def screensaverService():
	folder, timeout = getArgs(sys.argv[1:])
	filenames = getFiles(folder)
	eogPid = None
	signal.signal(signal.SIGTERM, killDaemon)

	while True:
		idletime = int(os.popen("xprintidle").read())/1000;
		if DEBUG:
			print(f'IdleTime = {idletime}')
		if idletime > timeout and eogPid is None:
			fn = filenames[random.randrange(len(filenames))]
			eogPid = sp.Popen(['eog','-f',fn])
		if idletime < timeout and eogPid is not None:
			eogPid.terminate()
			eogPid = None
		sleep(1)

if __name__ == "__main__":
	#daemon = Daemonize(app='GifSaver', pid=pidPath, action=screensaverService)
	#daemon.start()
	screensaverService()
