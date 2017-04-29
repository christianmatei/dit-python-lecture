import json

from http.client import HTTPConnection

PORT = 80
HOST = 'http://demo4866252.mockable.io'


class UsersClient(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def list(self):
        client = HTTPConnection(self.host, self.port)
        url = '{}/users'.format(self.host)

        client.request(method='GET', url=url)
        response = client.getresponse()
        print(response.status, response.reason)

        if response.status == 200:
            return json.loads(response.read())

    def get(self, id):
        client = HTTPConnection(self.host, self.port)
        url = '{}/users/{}'.format(HOST, id)

        client.request(method='GET', url=url)
        response = client.getresponse()
        print(response.status, response.reason)

        if response.status == 200:
            return json.loads(response.read())


if __name__ == '__main__':
    users_client = UsersClient(HOST, PORT)
    print(users_client.list())
    print(users_client.get(234298))
    print(users_client.get(234342))
