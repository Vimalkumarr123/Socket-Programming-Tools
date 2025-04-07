import socket

from lxml.xslt import message


def udp_client():
    host = input("Enter the server ip : ")
    port = 12346


    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            message = input("enter message (or 'quit' to exit )")
            if message == 'quit' :
                break
            s.sendall(message.encode(), (host,port))
            data,addr = s.recvfrom(1024)
            print(f"server response : {data}")

if __name__ == '__main__':
    udp_client()
    