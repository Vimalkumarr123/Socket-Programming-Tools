import socket
import threading

from websockets.legacy.protocol import broadcast

clients ={}

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected ")
    username = conn.recv(1024).decode()
    clients[username] = conn

    broadcast(f"{username} has joined the chat!", server =True)

    while True :
        try:
            message =conn.recv(1024).decode()
            if message == "/quite":
                break
            broadcast(f"{username}:{message}")

        except :
            break

    del clients[username]
    conn.close()
    broadcast(f"{username} left the chat.", server = True)
    print(f"[disconnected] {addr} disconnected")

def broadcast(message, server = False):
    prefix = ["server"] if server else ""
    full_message = f"{prefix} + {message}"
    print(full_message)
    for client in clients.values():
        try:
            client.send(full_message.encode())

        except :
            continue

def chat_server():
    host = "127.0.0.1"
    port = 4446

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen(1)
        print(f"[server] chat server listening on {host}:{port}")


        while True:
            conn, addr =s.accept()
            thread = threading.Thread(target=handle_client,args=(conn,addr))

            thread.start()

if __name__ == "__main__":
    chat_server()


