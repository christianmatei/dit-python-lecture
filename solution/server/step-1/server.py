from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = '127.0.0.1'


class UsersApi(BaseHTTPRequestHandler):

    def do_GET(self):

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))


if __name__ == '__main__':
    server_address = (HOST, PORT)
    print('starting server on %s:%s...' % server_address)

    httpd = HTTPServer(server_address, UsersApi)
    httpd.serve_forever()
