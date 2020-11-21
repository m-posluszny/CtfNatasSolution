import requests
import re
import base64

name = "natas8"

url = f"http://{name}.natas.labs.overthewire.org"
auth = (f"{name}","DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe")
secret = "3d3d516343746d4d6d6c315669563362"
secret = bytearray.fromhex(secret).decode()
secret = secret[::-1]
secret.encode('ascii')
secret = base64.b64decode(secret)
secret = secret.decode('ascii')
session = requests.session()

logon = session.post(url,auth=auth,data={'secret':secret,'submit':''})
regex = re.compile(r'The password for natas9 is ([\w\d]+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    ...
    
"""Natas 8

Harder variation of Natas 6.
This time in source code we could find this function:
function encodeSecret($secret) { return bin2hex(strrev(base64_encode($secret))); }
Which is basically encoding our key by just using base64 encoding, then reversing encoded string
and finally changing our string to hexadecimals value. All we need to do is to reverse it.
After providing it to post request password appeared.

"""
