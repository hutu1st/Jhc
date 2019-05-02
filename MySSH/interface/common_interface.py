from db import modules


def get_all_server_info():
    all_server_dic = modules.Server.get_server_dic()[0]
    return all_server_dic
