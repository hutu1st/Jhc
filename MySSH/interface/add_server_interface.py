from db import modules


def add_server(alias, username, password, address, port):
    server = modules.Server( alias, username, password, address, port)
    server.save()
    return server
