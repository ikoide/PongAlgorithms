import os, datetime

time = datetime.datetime.now()

os.system("git add .")
os.system("git commit -m '{time}'")
os.system("git push -u origin master")