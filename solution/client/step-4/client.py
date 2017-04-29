import json

from http.client import HTTPConnection

PORT = 80
HOST = 'http://demo4866252.mockable.io'


class User(object):

    def __init__(self, id, created, first_name, last_name):
        self.id = id
        self.created = created
        self.first_name = first_name
        self.last_name = last_name


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
            # Iterate the list creating a new user for each item
            users = []
            for data in json.loads(response.read()):
                users.append(User(**data))
            return users

    def get(self, id):
        client = HTTPConnection(self.host, self.port)
        url = '{}/users/{}'.format(HOST, id)

        client.request(method='GET', url=url)
        response = client.getresponse()
        print(response.status, response.reason)

        if response.status == 200:
            data = json.loads(response.read())
            return User(**data)


if __name__ == '__main__':
    users_client = UsersClient(HOST, PORT)
    print(users_client.list())
    print(users_client.get(234298).first_name)
    print(users_client.get(234342).first_name)
