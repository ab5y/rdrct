from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from webob import Response

DEBUG = True

def rdrct_to_www(request):
	return Response(status_int=302, location="http://www.thepolit.com")

# Move the application object here.
# Create a configurator to make *wsgi application*
config = Configurator()
config.add_view(rdrct_to_www)

# The "app" object to be exposed
app = config.make_wsgi_app()

if __name__ == '__main__':
	# config = Configurator()
	# config.add_view(rdrct_to_www)
	# app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8081, app)
	server.serve_forever()
