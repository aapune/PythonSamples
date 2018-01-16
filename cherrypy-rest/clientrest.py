"""
    Python / CherryPy / REST API
    Sample REST in cherryPy
    
    author - Aniruddha Anikhindi
"""
import cherrypy

clients = {
    '100': {
        'name': 'Mark Anderson',
        'address': 'New York'
    },

    '101': {
        'name': 'Mike Memoli',
        'address': 'New Jersey'
    },

    '102': {
        'name': 'Sam Mathur',
        'address': 'Chicago'
    }
}


class Client(object):
    exposed = True

    def GET(self, client_id=None):
        if client_id is None:
            return('No client ID is provided')
        elif client_id in clients:
            client = clients[client_id]
            return('Client with the ID %s is  %s, and the address of this client is %s' %
                   (client_id, client['name'], client['address']))
        else:
            return('No client with the ID %s :-(' % client_id)

if __name__ == '__main__':
    cherrypy.tree.mount(Client(), '/api/clients', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
