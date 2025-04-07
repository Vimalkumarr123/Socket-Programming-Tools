import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip,port):
    try :
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
            s.settimeout(1)
            result =s.connect_ex((ip,port))
            if result == 0 :
                print(f"Port{port} is open")
                return port

    except :
        return None

def port_scanner():
    target_ip = (input("Enter Target IP : "))
    start_port = int(input("Enter Start Port : "))
    end_port = int(input("Enter End Port : "))

    print(f"\n Scanning {target_ip} from port {start_port} to {end_port}.....")
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = [executor.submit(scan_port,target_ip,port) for  port in range(start_port,end_port + 1)]

        for future in  results:
            if future.result() is not None :
                open_ports.append(future.result())

    print("\nScan complete!")
    print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    port_scanner()