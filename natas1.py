import requests
import re

url = "http://natas1.natas.labs.overthewire.org"

auth = ("natas1","gtVrDuiDfck831PqWsLEZy5gyDz1clto")

session = requests.session()

logon = session.post(url,auth=auth)
regex = re.compile(r'password for natas2 is (\S+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    ...

"""Natas 1
This one wasn't any harder than the Natas0. Site told me
that I can't use ppm to view source code but it doesn't matter
for python :D
So I grabbed the password same way

"""