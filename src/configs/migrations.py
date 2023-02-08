import os

from flask_migrate import Migrate


directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'migrations')

migrate = Migrate(directory=directory)
