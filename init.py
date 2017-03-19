import socket

sock = socket.socket()
host = "localhost"
port = 1337

sock.bind((host,port))

print("listening")
sock.listen(5)

connections []
macs []

while(1):
    c, addr = sock.accept()
    print ("Got connection from " + str(addr))
    mac = c.recv(2048)
	connections.append(c)
	mac.append(c)
	
	if len(connections) > 1 :
		#ready to start a fight
		#play some sound 
		#print fight beginning
		#create player 1 monster
		#create player 2 monster
		#fight
	