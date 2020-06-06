from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Comment

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell #shell is used to test features in our app and for debugging
def make_shell_context():
    return dict(app = app,db = db,User = User, Comment= Comment )

if __name__ == '__main__':
    manager.run()