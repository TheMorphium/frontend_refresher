# frontend_refresher


Simple tool to check github for changes  If changes are found, run "npm run build", and then "pm2 restart all".  Can be automated with cron.

pip install requirements.txt

Create a .env file using the example.  Tool will also create a file called .lasthash to use to determine if folders contents have changed.