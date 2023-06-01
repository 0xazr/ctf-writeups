#!/usr/bin/env python3

import requests

url = 'http://206.189.236.145:9000/'

r = requests.post(url, {
	'note_title': 'fflflagaglag',
	'note': 'a'
	})

print(r.text)