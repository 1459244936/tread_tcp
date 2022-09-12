import socket 
if __name__ == '__main__':
#AF_INET指的是ipv4地址，SOCK_STREAM指的是tcp传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect('192.168.1.5',9090)
    send_content = "hellow"
    send_data = send_content.encode('gbk')
    tcp_client_socket.send(send_content)
    tcp_client_socket.recv(1024)
    tcp_client_socket.close()


     