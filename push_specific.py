import os, datetime

time = datetime.datetime.now()

files = input("File(s): ")
branch = input("Branch: ")

add = f"git add {files}"
commit = f"git commit -m '{time}'"
push = f"git push -u origin {branch}"

os.system(add)
os.system(commit)
os.system(push)