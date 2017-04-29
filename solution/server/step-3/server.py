import re
import json

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = '127.0.0.1'


users = {
    '234342': {
        'id': 234342,
        'created': '2016-09-10 11:20:42.143590',
        'first_name': 'Peter',
        'last_name': 'Griffen'
    },
    '234298': {
        'id': 234298,
        'created': '2016-05-10 20:18:29.451250',
        'first_name': 'Homer',
        'last_name': 'Simpson'
    }
}


class UsersApi(BaseHTTPRequestHandler):

    def _list_users(self):
        return json.dumps(list(users.values()))

    def _get_user(self, id):
        user = users.get(id)
        if user:
            return json.dumps(user)

    def _with_response_code(self, code):
        # Send response status code
        self.send_response(code)

        # Send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _write(self, data):
        self.wfile.write(bytes(data, "utf8"))

    def do_GET(self):
        if self.path == '/users':
            self._with_response_code(200)
            self._write(self._list_users())

        elif re.match('/users/[0-9]+$', self.path):
            id = self.path.split('/')[-1:][0]  # Grab the last value
            user = self._get_user(id)
            if user:
                self._with_response_code(200)
                self._write(user)
            else:
                self._with_response_code(404)

        else:
            self._with_response_code(404)


if __name__ == '__main__':
    server_address = (HOST, PORT)
    print('starting server on %s:%s...' % server_address)

    httpd = HTTPServer(server_address, UsersApi)
    httpd.serve_forever()
