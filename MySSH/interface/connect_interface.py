from db import modules


def connect(index):
    server_info = modules.Server.select(index)
    alias = server_info['alias']
    username = server_info['username']
    password = server_info['password']
    address = server_info['address']
    port = server_info['port']
    server = modules.Server(alias, username, password, address, port)
    server.connect()
