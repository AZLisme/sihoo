# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from datetime import datetime

from flask import Blueprint, request, render_template
from flask import redirect
from flask_socketio import send, join_room, leave_room

from sihoo.ext.socketio import socketio
from sihoo.models.chatroom import add_user, rm_user, add_message, add_chatroom

blue_print = Blueprint('sihoo.chatroom', __name__, template_folder='templates')

# 处理Socket链接信息

@socketio.on('connect')
def on_connect():
    print('User connected')


@socketio.on('disconnect')
def on_disconnect():
    print('User disconnect')


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    add_user(username, room)
    send("{} 加入了房间".format(username), room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    rm_user(username, room)
    send("{} 离开了房间".format(username), room=room)


@socketio.on('chat_msg')
def on_chat_msg(data):
    room = data['room']
    content = data['content']
    username = data['username']
    add_message(room, username, content)
    send("{} - {}: {}".format(datetime.now().strftime('%d %b %H:%M:%S'), username, content), room=room)


# 处理页面

@blue_print.route('/chat', endpoint='chat', methods=['GET'])
def chat():
    room = request.args['room']
    return render_template('chatroom.html', room_name=room)


@blue_print.route('/chat/add', endpoint='add_chat', methods=['GET', 'POST'])
def add_chat():
    if request.method == 'GET':
        return render_template("add_chatroom.html")
    else:
        name = request.form['name']
        add_chatroom(name=name)
        return redirect('/plaza')

# 处理API