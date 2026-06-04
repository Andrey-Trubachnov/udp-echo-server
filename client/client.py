import socket
import time

SERVER_HOST = 'echo-server'
SERVER_PORT = 8888
MESSAGE = "Привет, UDP!"

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.sendto(MESSAGE.encode(), (SERVER_HOST, SERVER_PORT))
        print(f"Отправлено: {MESSAGE}")
        
        client.settimeout(2)
        try:
            data, _ = client.recvfrom(1024)
            print(f"Ответ сервера: {data.decode()}")
        except socket.timeout:
            print("Нет ответа от сервера")
    
    time.sleep(5)