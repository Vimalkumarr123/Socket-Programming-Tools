import socket

def tcp_server():
    host = ("")
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.blind((host,port))
        s.listen(1)
        print(f"TCP server was listening on {host}:{port}}")

        conn,addr = s.accept()

        with conn :
            print(f"connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data :
                    break
                print(f"received: {data.decode().strip()}")
                conn.send(b"message recived")


if __name__ == "__main__":
    tcp_server()
