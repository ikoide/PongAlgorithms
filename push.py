import os, datetime

time = datetime.datetime.now()
commit = f"git commit -m '{time}'"

os.system("git add .")
os.system(commit)
os.system("git push -u origin master")