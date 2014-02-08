'''
MySQL Database Backuper
Authors: Hristo Dimitrov (hdimitrov.eu) & Yasen Georgiev (ygeorgiev.com)
Licence: MIT
Date published: 08 February 2014
'''

import subprocess,time

username="user" # DB User
password="pass" # DB Pass
dbs=["db1", "db2"] # Databases you want to backup
mysqldump_location="C:/xampp/mysql/bin/mysqldump.exe" # mysqldump location
files_location = "./" # Backup location

while 1:
    for db in dbs:
        if password=="":
            o=subprocess.check_output(mysqldump_location+" --opt -u "+username+" "+db)
        else:
            o=subprocess.check_output(mysqldump_location+" --opt -u "+username+" -p"+password+" "+db)
        open(files_location+db+'.sql','wb').write(o)
        
    log_file = open(files_location+"db_backups.log", "a")
    log_file.write(str(time.time())+" >> Created new backup\n")
    log_file.close()
    
    time.sleep(3600)
