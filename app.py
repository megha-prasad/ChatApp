from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__,template_folder='../templates')
app.config["MONGODB_SETTINGS"] = {
	"db":"chat_room",
	"host":"localhost",
	"port":27017
}
app.secret_key = b'_5#y2L"Fjnmb\n\xec]/'
db =  MongoEngine(app)
