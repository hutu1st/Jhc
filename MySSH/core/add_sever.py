from interface import add_server_interface


def add_server():
    while True:
        alias = input('输入主机别名：(quit by q)').strip()
        if alias == 'q': return
        if not alias:
            print('不能为空！重新输入')
            continue
        break
    while True:
        address = input('输入ip地址：(quit by q)').strip()
        if address == 'q': return
        if not address:
            print('不能为空！重新输入')
            continue
        break
    while True:
        username = input('输入用户名：(quit by q)').strip()
        if username == 'q': return
        if not username:
            print('不能为空！重新输入')
            continue
        break
    while True:
        password = input('输入密码：(quit by q)').strip()
        if password == 'q': return
        if not password:
            print('不能为空！重新输入')
            continue
        break
    while True:
        port = input('输入端口号，不输，默认为22：(quit by q)').strip()
        if port == 'q': return
        if not port:
            print('已设置为默认22端口')
            port = '22'
        break
    server = add_server_interface.add_server(alias, username, password, address, port)
    if server:
        return print('添加成功！')
