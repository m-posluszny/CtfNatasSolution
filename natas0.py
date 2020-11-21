#%%
import requests
import re

url = "http://natas0.natas.labs.overthewire.org"

auth = ("natas0","natas0")

session = requests.session()

logon = session.post(url,auth=auth)
regex = re.compile(r'password for natas1 is (\S+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    ...

"""
Natas0 is pretty simple
    To connect to the site I am using requests,
    after creating session object I am sending post http request
    with http basic auth parameters as login ans password stored in tuple
    then I am searching for password using regex.
    Before doing that I printed http response to see where the password is.
    
"""
