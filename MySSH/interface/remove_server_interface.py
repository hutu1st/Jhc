from db import modules


def remove_server_interface(index):
    modules.Server.remove_server(index)
