from app import create_app,db
from flask_script import Server,Manager 
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Comment,Post

app=create_app('development')

manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Comment=Comment,Post=Post)

@manager.command
def test():
    import unittest
    test=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__=="__main__":
    manager.run()