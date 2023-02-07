from datetime import datetime

from flask import Flask


server = Flask(__name__)

@server.get("/")
def index():
    with open("logs.txt", "a") as file:
        file.write(datetime.now().isoformat())
    return {"ok": 'nathan batista'}

