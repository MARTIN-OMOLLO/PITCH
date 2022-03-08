from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User

app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
# manager.add_command('server'server(use_debugger=True))

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)
    

@manager.add_command
def test():
    import unittest
    tests = unittest,TestLoader().discover('test')
    # unittest.TextTestRunner(verbosity = 3).return

    if __name__ == "__main__":
        manager.run()