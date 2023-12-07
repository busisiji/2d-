import socket

class Client(object):
    def __init__(self,ip,port):
        # 1 创建客户端套接字对象(买电话)
        # 参数1: ipv4(ip协议的版本)
        # 参数2: 选择协议(SOCK_STREAM==> tcp协议)
        self.tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2 和服务端套接字建立连接(打电话)
        # 参数: 元组(有两个元素!!!)
        # 元素1: 服务器的IP地址(字符串)
        # 元素2: 服务器的端口号(数字)
        self.tcp_client_socket.connect((ip, port))

    def send(self,result):
        # 发送数据的时候需要先转化成二进制
        data = str(result)
        # 编码
        data = data.encode("utf8")
        # 3 发送数据(说话)
        self.tcp_client_socket.send(data)
    def rece(self):
        # 4 接收数据(聆听)
        # 参数: 以字节为单位的接受的数据的大小
        # 注意: recv会阻塞等待数据的到来
        recv_data = self.tcp_client_socket.recv(1024)
        # 解码
        recv_data = recv_data.decode("utf8")
        print('接收到：',recv_data)
    def close(self):
    # 5 关闭客户端套接字
        self.tcp_client_socket.close()

if __name__ == '__main__':
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description='Simple Wave Audio Recorder',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ip', default="192.168.1.47", help='ip')
    parser.add_argument('--port',  default=8899,help='port')
    args = parser.parse_args()
    client = Client(args.ip, args.port)
    client.send('hello world')
    client.rece()