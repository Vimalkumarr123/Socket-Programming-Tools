import socket

def banner_grabber():
    target_ip = input("enter a target ip :")
    target_port = input("enter a target port :")

    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((target_ip,target_port))
            s.send(b"GET / HTTP/1.1\r\n\r\n")
            banner = s.recv(1024).decode().strip()
            print(f"\n banner from {target_ip}:{target_port}:")
            print("_"* 50)
            print(banner)
            print("_" * 50)

    except Exception as e:
        print(f"erorr: {e}")

if __name__ == "__main__":
    banner_grabber()