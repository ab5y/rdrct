# import application from py file
# eg from wsgi import application
from application import app

import cherrypy

if __name__ == '__main__':
	# Mount the application (or app)
	cherrypy.tree.graft(app, "/")
	
	# Unsubscribe the default server
	cherrypy.server.unsubscribe()

	# Instantiate a new server object
	server = cherrypy._cpserver.Server()

	# Configure the server object
	server.socket_host = "0.0.0.0"
	server.socket_port = 8081
	server.thread_pool = 30

	# Subscribe this server
	server.subscribe()

	# Start the server engine
	cherrypy.engine.start()
	cherrypy.engine.block()
