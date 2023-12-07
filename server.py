import socket


def handler_client_request(client_socket):
    """处理客户端请求"""

    while True:
        # 5 接收数据
        # 参数:接受数据的大小(节)
        try:
            client_data = client_socket.recv(1024)
        except:
            print("客户端关闭了!!!")
            break
        # 如果接受到的数据长度为0 则证明客户端关闭
        if len(client_data) == 0:
            print("客户端关闭了!!!")
            break

        # 对二进制的数据解码
        client_data = client_data.decode()
        print(client_data)
        if client_data == 'hello world':
            # 6 发送数据
            send_data = "123".encode()
            client_socket.send(send_data)

    client_socket.close()


def main():
    # 1 创建服务端端套接字对象
    # 参数1: ipv4
    # 参数2: tcp协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用设置作用: 一旦服务端关闭 端口立马释放
    # setsocketopt : 设置socket选项
    # 参数1: socket选项列表(SOL)
    # 参数2: 地址复用
    # 参数3: True:开启选项 False:不开启选项(默认都是不开启的)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2 绑定端口号
    # 参数: 元组(两个元素) 元素1:IP地址(字符串) 元素2:端口号(数字)
    # 192.168.144.28(服务器的IP地址)
    # 不写默认就是本机ip地址(127.0.0.1)
    tcp_server_socket.bind(("192.168.1.47", 8899))
    # 3 设置监听
    # 参数:最大监听个数(排队处理的最大等待数量)
    # tcp_server_socket从主动套接字变成了被动套接字
    tcp_server_socket.listen(128)

    while True:
        # 4 阻塞等待接受客户端的连接请求
        # <返回值> 是一个元组(有两个元素):
        # 元素1 和客户端进行通讯的socket 元素2: 客户端的地址信息(ip,port)
        # 返回值是一个元组 通过拆包语法 我们分别获取了 元素1 和 元素2
        client_socket, client_addr = tcp_server_socket.accept()

        # 处理客户端的请求
        handler_client_request(client_socket)

    # 7 关闭套接字
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
