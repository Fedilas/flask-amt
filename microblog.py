from app import create_app, db, cli, socketio
from app.models import User, Post, Message, Notification, Task, Chat
app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task, 'Chat': Chat}




if __name__ == '__main__':
    socketio.run(app)
