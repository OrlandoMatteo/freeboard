import cherrypy
import json
import os
class ClientREST(object):
    """docstring for Reverser"""
    exposed=True
    def __init__(self):
            pass
    def GET(self,**params):
        return open('index.html')
    def POST(self, *uri, **params):
        config=params['json_string']
        f=open ("dashboard/dashboard.json", "w")
        f.write(config)
        f.close()

if __name__ == '__main__':
    conf = {
	'/':{
		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
		'tools.staticdir.root': os.path.abspath(os.getcwd()),	#command taken from slides
		},
	'/css':{
		'tools.staticdir.on': True,
		'tools.staticdir.dir':'./css'
		},
	'/dashboard':{
		'tools.staticdir.on': True,
		'tools.staticdir.dir':'./dashboard'
		},
	'/img':{
		'tools.staticdir.on': True,
		'tools.staticdir.dir':'./img'
		},
	'/js':{
		'tools.staticdir.on': True,
		'tools.staticdir.dir':'./js'
		},
	'/plugins':{
		'tools.staticdir.on': True,
		'tools.staticdir.dir':'./plugins'
		}
	}
    cherrypy.config.update({
        "server.socket_port": 8088,
        })
    cherrypy.tree.mount(ClientREST(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
