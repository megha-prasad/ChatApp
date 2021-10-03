import app
from room_det import create_room,add_room_members,get_rooms,get_room_members,delete_room,remove_room_member

app.add_url_rule("/create_room",view_func=create_room,methods=["GET","POST"])
app.add_url_rule("/add_room_members",view_func=add_room_members,methods=["GET","POST"])
app.add_url_rule("/get_rooms",view_func=get_rooms,methods=["GET","POST"])
app.add_url_rule("/get_room_members",view_func=get_room_members,methods=["GET","POST"])
app.add_url_rule("/delete_room",view_func=delete_room,methods=["GET","POST"])
app.add_url_rule("/remove_room_member",view_func=remove_room_member,methods=["GET","POST"])