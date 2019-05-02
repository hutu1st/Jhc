from core import add_sever, connect, remove_server
import os

fn_map = {
    '0': {'fn': add_sever.add_server, 'fn_info': '添加主机'},
    '1': {'fn': connect.connect, 'fn_info': '连接主机'},
    '2': {'fn': remove_server.remove_server, 'fn_info': '删除主机'},

}


def run():
    os.system('clear')
    while True:
        print('MySSH'.center(50, '*'))
        for k, v in fn_map.items():
            print('%s %s' % (k, v['fn_info']))
        choice = input('Enter your choice:(quit by q)').strip()
        if choice == 'q':
            return
        if choice not in fn_map:
            print('Invalid choice! Choose again')
            continue
        fn_map[choice]['fn']()
