from interface import connect_interface
from core import common
import os


def connect():
    msg, all_server_dic = common.print_server_list()
    if not msg:
        return
    os.system('clear')

    while True:
        print('选择连接主机'.center(50, '='))
        print(msg)
        while True:
            choice = input('选择需要连接的主机:(quit by q)').strip()
            if choice == 'q':
                os.system('clear')
                return
            if choice not in all_server_dic:
                print('选择无效！重新选择')
                continue
            break
        os.system('clear')
        connect_interface.connect(choice)
