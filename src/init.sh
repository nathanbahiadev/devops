#!/bin/sh
flask db init
flask db migrate
flask db upgrade
gunicorn -b 0.0.0.0:8000 -w 4 src.app:server
