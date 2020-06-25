from wsgiref.simple_server import make_server


def application(env, start_response):
    """
    A basic WSGI application
    """

    start_response("200 OK", [("Content-Type", "text/html")])

    import ipdb

    ipdb.set_trace()

    return [b"Hello World"]


if __name__ == "__main__":
    make_server("", 8000, application).serve_forever()
