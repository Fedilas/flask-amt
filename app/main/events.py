# # from flask import session
# #
# # from flask_socketio import emit, join_room, leave_room
# # from .. import socketio
# # from app.models import Chat
# # from app import db
# #
# #
# #
# # @socketio.on('joined', namespace='/explore')
# # def joined(message):
# #     """Sent by clients when they enter a room.
# #     A status message is broadcast to all people in the room."""
# #     room = session.get('room')
# #     join_room(room)
# #     emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)
# #
# #
# # @socketio.on('text', namespace='/explore')
# # def text(message):
# #     """Sent by a client when the user entered a new message.
# #     The message is sent to all people in the room."""
# #     room = session.get('room')
# #     chat = message['msg']
# #     emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
# #     c = Chat(body=chat)
# #     db.session.add(c)
# #     db.session.commit()
#
#
#
#
#
#
# @socketio.on('left', namespace='/explore')
# def left(message):
#     """Sent by clients when they leave a room.
#     A status message is broadcast to all people in the room."""
#     room = session.get('room')
#     leave_room(room)
#     emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)
