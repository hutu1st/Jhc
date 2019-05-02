from interface import remove_server_interface
from core.common import print_server_list
import os


def remove_server():
    while True:
        msg, all_server_dic = print_server_list()
        if not msg:
            return
        os.system('clear')
        print('删除主机'.center(50, '='))
        print(msg)
        while True:
            choice = input('选择需要删除的主机:(quit by q)').strip()
            if choice == 'q':
                os.system('clear')
                return
            if choice not in all_server_dic:
                print('选择无效！重新选择')
                continue
            break
        remove_server_interface.remove_server_interface(choice)
        print('删除成功！')
