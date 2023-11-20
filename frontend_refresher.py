#!/usr/bin/python3


import os
from dotenv import load_dotenv
import subprocess
import git
from datetime import datetime
import logging



load_dotenv()
npm_build = 'npm run build'
monitored_directory = os.getenv('monitored_directory')
script_folder = os.getenv('script_folder')
logfile = f'{script_folder}/refresh_log.log'



logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler(logfile, 'a'))
print = logger.info

def check_for_updates():
    gitfolder = git.cmd.Git(monitored_directory)
    return gitfolder.pull() != 'Already up to date.'


def rebuild_web_site():
    os.chdir(monitored_directory)
    result = subprocess.check_call('npm run build', shell=True)
    result = subprocess.check_call('pm2 restart all', shell=True)


def run_check():
    current_time = datetime.now().strftime("%m-%d-%Y_%Hh%Mm%Ss")
    print(f'Checking for updates at {current_time}')
    if check_for_updates():
        rebuild_web_site()


run_check()