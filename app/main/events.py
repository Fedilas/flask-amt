from flask import session
from flask_login import current_user

from flask_socketio import emit, join_room, leave_room
from .. import socketio
from app.models import Chat, GlobalChat
from app import db



@socketio.on('joined', namespace='/explore')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/explore')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    db.create_all() ## massively important!!
    room = session.get('room')
    group = current_user.room
    chat = str(message['msg'])
    user = current_user.username
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
    c = Chat(body=chat, room=group, user=user)

    db.session.add(c)
    db.session.commit()


@socketio.on('left', namespace='/explore')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)



######## globalchat

@socketio.on('joined', namespace='/user')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/user')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    db.create_all() ## massively important!!
    room = session.get('room')

    globalchat = str(message['msg'])
    user = current_user.username
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
    c = GlobalChat(body=globalchat, user=user)

    db.session.add(c)
    db.session.commit()


@socketio.on('left', namespace='/user')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

