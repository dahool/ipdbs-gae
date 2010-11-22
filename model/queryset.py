from model.models import Log, Server

class ServerQuerySet():
    
    def get_by_serverkey(ukey)
        q = Server.filter('ukey = ', ukey)
        return q.get()
        
    def update_servercount(server, count):
        server.play_num = count
        server.put()

    def update_servername(server, name):
        server.name = name
        server.put()

class LogQuerySet():
    
    def fetch_by_guid(guid, server=None, limit=1000, offset=0, count=False):
        # todo impl cache
        q = Log.filter('guid = ', guid)
        if server:
            q = q.filter('server = ', server)
        if count:
            return q.count(limit)
        return q.fetch(limit, offset)
    
    def fetch_by_datesince(date, server=None, limit=1000, offset=0, count=False):
        q = Log.filter('time_edit >= ', date)
        if server:
            q = q.filter('server = ', server)
        if count:
            return q.count(limit)
        return q.fetch(limit, offset)

    def fetch_by_all(ip, nick, guid, server, limit=1000, offset=0, count=False):
        q = Log.filter('ip = ', ip).filter('nick = ', nick).filter('server = ', server).filter('guid = ', guid)
        if count:
            return q.count(limit)
        return q.fetch(limit, offset)
