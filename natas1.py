#%%
import requests
import re

url = "http://natas1.natas.labs.overthewire.org"

auth = ("natas1","gtVrDuiDfck831PqWsLEZy5gyDz1clto")

session = requests.session()

logon = session.post(url,auth=auth)
passwd = re.findall(r'password for natas\d is (\S+)',str(logon.content))[0]
print(passwd) 

"""Natas 1
This one wasn't any harder than the Natas0. Site told me
that I can't use ppm to view source code but it doesn't matter
for python :D
So I grabbed the password same way

"""