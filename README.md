# DIT Python Lecture

This lecture will aim to cover some very basic [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles while also introducing us to the Python programming language. We will be creating a simple client and server in python, but before we begin, ensure [Python 3.6.1](https://www.python.org/downloads/) is installed on your system. Verify by running the following command in your terminal:

```bash
$ python -V
Python 3.6.1
```

Sometimes you may need to explicity say you are using Python 3, so if the above command returns `Python 2.7.x` you may need to run as:

```bash
$ python3 -V
Python 3.6.1
```

If running `Python3` still returns you an older version of Python, update it using the instructions outlined at the bottom of this page. If it's the case where you need to use `python3`, make sure to run the client and server run as `python3 client.py` and `python3 server.py`. Go to the bottom of the page for some help on installing Python.

Once Python has been setup, we will be looking at the following sections:

- Interacting with a mock REST service.
- Building a Python client for the above mock REST service.
- Building a Python server that serves data to the client in order to replace the mock service.

## Step 1 - Interacting With Mock REST Service

The mock REST service uses [https://www.mockable.io](https://www.mockable.io) to serve static dummy data. This can be very useful for developers building clients before any backend systems exist. Ensure it is working for you by running a `curl` command on the following endpoints:

- [http://demo4866252.mockable.io/users](http://demo4866252.mockable.io/users)
- [http://demo4866252.mockable.io/users/234298](http://demo4866252.mockable.io/users/234298)
- [http://demo4866252.mockable.io/users/234342](http://demo4866252.mockable.io/users/234342)

When interacting with these, can you:

- Tell what HTTP method is used (`GET`/`POST`/`PUT`/`PATCH`)?
- List all the headers returned?

## Step 2 - Build a client

Now that we can pull data from the above mock endpoints, we can start creating a simple Python client. Lets break this into a number of small tasks. In this step we are going to be using two Python 3 modules, [HTTPConnection](https://docs.python.org/3/library/http.client.html) and the [json](https://docs.python.org/3/library/json.html) library. Start implementing your code in the `client.py` file

- Import the `HTTPConnection` module, and use it to make a request to the above URLs.
- When you can successfully make a request and print the raw response as a string, use the `json` module to decode that into a native python data type (as in `list` and `dict`).
- Now we figured out how to represent the data to something meaningful, create a client class called `UsersClient` to encapsulate the logic for making remote calls.
- Finally, instead of having the data represented as native Python data types, lets create a `User` class to encapsulate the returned data from the API.

## Step 3 - Build a server

Now lets build a server to serve the same data. Just like when creating the client, we can break this into small tasks. We will be making use of the [HTTPServer](https://docs.python.org/3/library/http.server.html) and once again the [json](https://docs.python.org/3/library/json.html) library. Start implementing your code in the `server.py` file

- To create a Http server, you will need to import `HTTPServer` to handle the actual server instance, and the `BaseHTTPRequestHandler` to handle incoming requests. Get something running so that you can make `curl` requests to it.
- Once we have something being served, lets implement the *list all users* endpoint (the `/users` endpoint). Ensure to also set the `Content-Type: application/json` header. Return the same static data the dummy endpoints return. Use the `json` library to encode Python's data types to JSON.
- Next see if we can implement the endpoint where we can get users by their Id. As in the `users/234298` and `users/234342` endpoint. Remember the Id should be dynamic, and if we don't have that Id, we should return `404 - Not Found`. There are a number of ways to extract the Id within the URL path, one being a `regex` pattern match.

# Python Installation

#### Mac OSX

See more [here](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/) or [here](https://www.python.org/downloads/), but basically using `brew` is probably the easiest option.

```bash
$ brew install python3
```

 If you run into linking issues, run:

 ```bash
 brew link --overwrite python3
 ```

#### Windows

Download and install Python from [here](https://www.python.org/downloads/). Once installed you should be able to run a Python shell. You then need to add Python to the system path, you can do this by:
- Opening `My Computer` > `Properties` > `Advanced System Settings` > `Environment Variables`
- Then edit the `Path` environment variable by appending `%USERPROFILE%\AppData\Local\Programs\Python\Python36-32` (or where ever your Python is installed on your PC). Ensure that each path entry is separated by a `;`.
- Test to ensure it works by opening a command prompt and typing `python -V`

If using windows, it is also recommend to use [cygwin](https://cygwin.com/) over the native windows command prompt, but for the purpose of this lecture, using the native command prompt should be ok.

#### Anything Else

Other unix like sytems should have python installed by default, just check the version is correct. When running `python3 -V`, the version may be a little older, perhps `3.4.x`. For the purpose of this lecture it may be ok, however it is reccomented to use `3.6.1` as this material was tested using that version.
