from interface import common_interface


def print_server_list():
    all_server_dic = common_interface.get_all_server_info()
    # print(all_server_dic)
    if not all_server_dic:
        return print("尚未添加主机！")
    line = "+{}+".format("-" * 50)
    msg = '%s\n' % line
    index_list = []
    for index in all_server_dic:
        index_list.append(index)
    index_list.sort()
    for i in index_list:
        alias = all_server_dic[i]['alias']
        username = all_server_dic[i]['username']
        address = all_server_dic[i]['address']
        port = all_server_dic[i]['port']
        msg += '%s Alias【%s】%s@%s port【%s】\n' % (i, alias, username, address, port)
    msg += '%s\n' % line
    return msg, all_server_dic
