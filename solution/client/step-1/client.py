from http.client import HTTPConnection

PORT = 80
HOST = 'http://demo4866252.mockable.io'

if __name__ == '__main__':
    client = HTTPConnection(HOST, PORT)

    url = '{}/users'.format(HOST)

    client.request(method='GET', url=url)
    response = client.getresponse()

    print(response.status, response.reason)
    print(response.read())
