from datetime import datetime

from flask import Flask


server = Flask(__name__)

@server.get("/")
def index():
    return {"ok": True}
