import socket 
if __name__ == '__main__':
#AF_INET指的是ipv4地址，SOCK_STREAM指的是tcp传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('192.168.1.7',7777))#应该是元组形式
    send_content = "我是你爹"
    send_data = send_content.encode("gbk")
    tcp_client_socket.send(send_data)#这里原来的错误是传的send_content,没有将字节encode
    recv_data = tcp_client_socket.recv(1024) #接受对方传输信息
    recv_content = recv_data.decode("gbk")
    print("对方回复的数据为：",recv_content)#需打印,但是这个前面的中文是乱码
    tcp_client_socket.close()
    #结束，这是个可运行，可实现文件


     