#membuat website
#beljar_web1.py

import wsgiref.simple_server

def application(environ, start_response):
    #response
    response = b"hello word"

    #status respon
    status = "200 ok"

    #header respon
    headers = [("content-type", "text/html")]

    #pengaturan status dan header
    start_response(status, headers)

    return [response]

if __name__ == "__main__":

    W_S = wsgiref.simple_server.make_server(
        host = "localhost",
        port = 8021,
        app = application

    )

    W_S.handle_request()
