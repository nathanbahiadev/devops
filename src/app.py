from flask import Flask, jsonify

from src.configs.settings import environment as EnvConfig
from src.configs.database import db
from src.configs.migrations import migrate


server = Flask(__name__)
server.config.from_object(EnvConfig)

db.init_app(server)
migrate.init_app(server, db)

from src.configs.database import PingModel


@server.get("/")
def index():
    db.session.add(PingModel())
    db.session.commit()

    pings = db.session.query(PingModel).all()
    response = [ping.as_dict() for ping in pings]
    
    return jsonify(response)
