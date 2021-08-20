#!/usr/bin/python3

import sys
import subprocess as sp
import os
import glob
import random
import signal
import argparse as ap
from time import sleep

# Pyinstaller Build Command = pyinstaller --onefile GifSaver.py

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
	parser.add_argument('-c', '--change', help='Change Image/GIF after seconds (0 = shuffle disable)', default=60, type=int)
	res = parser.parse_args()
	if DEBUG:
		print('Arguments:')
		print(f'Folder = {res.folder}')
		print(f'Timeout = {res.timeout}')
		print(f'Change = {res.change}')
	return (res.folder, res.timeout, res.change)

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
	folder, timeout, change = getArgs(sys.argv[1:])
	filenames = getFiles(folder)
	eogPid = None
	changetime = 0
	signal.signal(signal.SIGTERM, killDaemon)

	while True:
		idletime = int(os.popen("xprintidle").read())/1000;
		if DEBUG:
			print(f'IdleTime = {idletime}')
		if idletime > timeout:
			if eogPid is None:
				fn = filenames[random.randrange(len(filenames))]
				eogPid = sp.Popen(['eog','-f',fn])
			if change != 0:
				changetime += 1
				if change == changetime:
					changetime = 0
					fn = filenames[random.randrange(len(filenames))]
					sp.Popen(['eog','-f','-w',fn])
		if idletime < timeout and eogPid is not None:
			eogPid.terminate()
			eogPid = None
			changetime = 0
		sleep(1)

if __name__ == "__main__":
	screensaverService()
