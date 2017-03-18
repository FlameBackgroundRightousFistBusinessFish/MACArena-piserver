import socket


sock = socket.socket()
host = "localhost"
port = 1337

sock.bind((host,port))

print("listening")
sock.listen()

while(1):
    c, addr = sock.accept()
    print ("Got connection from " + str(addr))

    print(c.recv(2048))

