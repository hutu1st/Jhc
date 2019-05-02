from db import db_handler
import pexpect


class Server:

    def __init__(self, alias, username, password, address, port):
        self.alias = alias
        self.username = username
        self.password = password
        self.address = address
        self.port = port
        self.index = self.get_server_dic()[1]

    @staticmethod
    def get_server_dic():
        all_server_list = db_handler.select()
        all_server_dic = {str(k): v for k, v in enumerate(all_server_list)}
        next_index = len(all_server_dic)
        return all_server_dic, str(next_index)

    @classmethod
    def select(cls, index):
        all_server_dic = cls.get_server_dic()[0]
        server_info = all_server_dic[index]
        return server_info

    def save(self):
        all_server_dic, index = self.get_server_dic()
        server_info = {
            "alias": self.alias,
            "address": self.address,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        all_server_dic[self.index] = server_info
        all_server_list = list(all_server_dic.values())
        db_handler.save(all_server_list)

    @staticmethod
    def remove_server(index):
        all_server_dic, next_index = Server.get_server_dic()
        all_server_dic.pop(index)
        all_server_list = list(all_server_dic.values())
        db_handler.save(all_server_list)

    def connect(self):
        cmd = 'ssh %s@%s -p %s' % (self.username, self.address, self.port)
        ssh = pexpect.spawn(cmd)
        ssh.setwinsize(51, 80)
        try:
            i = ssh.expect(["(?i)Password.*", "(?i)continue.*", "~"], timeout=5)
            if i == 0:
                ssh.sendline(self.password)
            if i == 1:
                ssh.sendline('yes\n')
                ssh.expect("(?i).*Password.*")
                ssh.sendline(self.password)
            if i == 2:
                print(ssh.before.decode())
            ssh.interact()
            print('溜了溜了～～')
        except pexpect.EOF:
            print("EOF,连接失败")
        except pexpect.TIMEOUT:
            print("TIMEOUT")
        finally:
            ssh.close()
