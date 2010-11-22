from google.appengine.ext import db

class Server(db.Model):
    name = db.StringProperty(default='')
    ukey = db.StringProperty()
    play_num = db.IntegerProperty()
    contact = db.StringProperty()
    time_add = db.DateTimeProperty(auto_now_add=True)
    time_edit = db.DateTimeProperty(auto_now=True)

class Log(db.Model):
    ip = db.StringProperty(default='0.0.0.0')
    nick = db.StringProperty(default='')
    time_add = db.DateTimeProperty(auto_now_add=True)
    time_edit = db.DateTimeProperty(auto_now=True)
    guid = db.StringProperty(default='')
    server = db.ReferenceProperty(Server)
    
