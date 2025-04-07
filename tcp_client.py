import socket

def tcp_client():
    host = input("Enter the host address: ")
    port = 12345

    try :
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host,port))
            while True:
                message = input("Enter the message (or 'quit' to exit )")
                if message == 'quit' :
                    break
                s.sendall(message.encode())
                data = s.recv(1024)
                print(f"server response : {data.decode()}")

if __name__ == "__main__":
    tcp_client()