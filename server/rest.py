from bottle import hook, response, route, run
from json import dumps
 
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/hello/:name')
def index(name='World'):
	return dumps([{'key':'value'}]);

run(host='localhost', port=8080)