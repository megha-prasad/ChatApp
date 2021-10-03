from flask_mongoengine import Document
from app import db
from flask import request,render_template
from datetime import datetime

class room_collection(Document) :
    room_name = db.StringField(required=True)
    created_by = db.StringField(required=True)
    created_at = db.DateTimeField(required=True)
    room_id = db.StringField(required=True)
class room_members_collection(Document):
    username = db.StringField(required=True)
    added_at = db.DateTimeField(required=True)

def create_room():
    if request.method == 'POST':
        room_name = request.form["room_name"]
        created_by = request.form["created_by"]
        created_at = datetime.now()
        room_collection.objects.create(room_name=room_name,created_by=created_by,created_at=created_at)
        return render_template("")
    return render_template("")

def add_room_members():
    if request.method == 'POST':
        room_id=request.form["room_id"]
        username = request.form("username")
        added_at = datetime.now()
        room_members_collection.objects.create(room_id=room_id,username=username,added_at=added_at)
        return render_template("")
    return render_template("")

def get_rooms():
    if request.method == 'GET':
        rooms=room_collection.objects.all().to_json()
        return render_template("",rooms=rooms)
    return render_template("")

def get_room_members():
    if request.method == 'GET':
        room_mem=room_collection.objects.all().to_json()
        return render_template("",room_mem=room_mem)
    return render_template("")

def delete_room():
    if request.method == 'POST':
        room_id=request.form["room_id"]
        room=room_collection.objects.get(id=room_id)
        room.delete()
        return render_template('')
    return render_template('')

def remove_room_member():
    if request.method == 'POST':
        room_id=request.form["room_id"]
        room_member=room_members_collection.objects.get(id=room_id)
        room_member.delete()
        return render_template('')
    return render_template('')




