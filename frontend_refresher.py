import logging
import os
from dotenv import load_dotenv
import subprocess
import git
from datetime import datetime
logging.basicConfig(filename='refresh_log.log', encoding='utf-8', level=logging.DEBUG)



load_dotenv()
npm_build = 'npm run build'
monitored_directory = os.getenv('monitored_directory')




def check_for_updates():
    gitfolder = git.cmd.Git(monitored_directory)
    changes_made = gitfolder.pull() != 'Already up to date.'
    return changes_made


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