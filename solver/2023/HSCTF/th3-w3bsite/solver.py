import requests
import re

url = "https://th3-w3bsite.hsctf.com/"

r = requests.get(url)
flag = re.findall(r"flag{.*}", r.text)[0]

print(flag)