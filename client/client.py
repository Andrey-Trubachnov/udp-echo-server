import socket
import time
import os

SERVER_HOST = os.getenv('SERVER_HOST', 'udp-server-service')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

count = 1

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        message = f'ping {count}'

        client.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
        print(f"Отправлено: {message}")
        
        client.settimeout(2)
        try:
            data, _ = client.recvfrom(1024)
            print(f"Ответ сервера: {data.decode()}")
        except socket.timeout:
            print("Нет ответа от сервера")
    
    count += 1
    time.sleep(int(os.getenv('MESSAGE_INTERVAL', 5)))
