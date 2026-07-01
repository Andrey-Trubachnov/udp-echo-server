import socket
import os


HOST = '0.0.0.0'
PORT = int(os.getenv('UDP_PORT', 8888))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))

    while True:
        data, addr = server.recvfrom(1024)
        print(f"Получено от {addr}: {data.decode()}")
        server.sendto(data, addr)
