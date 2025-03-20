#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
# author : CaptainMGC 
# Tested on Windows / Linux / Android (Termux)
# Simple script for install CyberScan

__author__ = "CaptainMGC"

import os
import subprocess
import sys

banner = '''
             
\033[92m 

 _____      _               _____                 
/ ____|    | |             / ____|                
| |    _   _| |__   ___ _ _| (___   ___ __ _ _ __  
| |   | | | | '_ \ / _ \ '__\___ \ / __/ _ | '_ \ 
| |___| |_| | |_) |  __/ |  ____) | (_| (_| | | | |
 \_____\__, |_.__/ \___|_| |_____/ \___\__,_|_| |_|
        __/ |                                      
       |___/   v1.0
                Update Script for CyberScan
           Created by CaptainMGC [ https://github.com/captainmgc ]

'''
print(banner)

content = """
#!/bin/bash

cd /usr/share/cyberscan
python3 cyberscan "$@"
"""

def main():
	if os.name != "nt":
		if os.getuid() == 0:
			os.system("git clone https://github.com/captainmgc/cyberscan /usr/share/cyberscan")
			for i in ["requests", "beautifulsoup4"]:
				subprocess.check_call([sys.executable, "-m", "pip", "install", i])
			
			with open("/usr/bin/cyberscan", "w") as file:
				file.write(content)
			
			os.system("chmod +x /usr/bin/cyberscan")

			print("\n\n[+] Update finished, Run \033[91m'cyberscan'\033[92m In Terminal!")
		else:
			print("Run as root!")
	else:
		print("This script doesn't work on Windows!")

if __name__ == "__main__":
	main()
