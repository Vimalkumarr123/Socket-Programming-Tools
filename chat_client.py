import socket
import threading

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("Disconnected from server.")
                break
            print(message)
        except ConnectionResetError:
            print("Connection reset by server.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def chat_client():
    host = input("Enter server IP: ")
    port = int(input("Enter server port: "))

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        username = input("Enter your username: ")
        client_socket.send(username.encode())

        print("Connected to chat server. Type /quit to exit.")

        # Start the receiving thread
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()

        while True:
            message = input()
            if message.strip() == "/quit":
                client_socket.send(message.encode())
                break
            client_socket.send(message.encode())

    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    chat_client()
