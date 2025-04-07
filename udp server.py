import  socket

def udp_server():
    host ="127.0.0.1"
    port = 12346

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.blind((host, port))
        s.listen(1)
        print(f"UDP server listening on {host}:{port}")

        while True:
            data,addr =s.recvfrom(1024)
            print(f"recived from {addr} :{data.decode()} ")
            s.sendto(b'message recived',addr)


if __name__ == '__main__':
    udp_server()
    