from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = '127.0.0.1'


if __name__ == '__main__':
    server_address = (HOST, PORT)
    print('starting server on %s:%s...' % server_address)
