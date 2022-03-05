from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User

app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)


