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
		

def buildMac (macaddress):
	chars = list(macaddress)
	#
	#use pygame to build image
	"""alW= 300
        alH = 600
        al_print = pygame.transform.scale(_alien.curr_alien,(alW,alH))
        pil_st_img = pygame.image.tostring(al_print, "RGBA",False)
        pil_img = Image.fromstring("RGBA",(alW,alH),pil_st_img)
        printer.printImage(pil_img)"""
		