import math

class macmac:

	def __init__(self, macAddress):
        macchars = list(macAddress)
		self.attack = list(str(floor((macchars[8] ^ 2) / math.pi)))[-1]
		self.defence = list(str(floor((macchars[9] ^ 2) / math.pi)))[-1]
		self.mAttack = list(str(floor((macchars[10] ^ 2) / math.pi)))[-1]
		self.mDefence = list(str(floor((macchars[11] ^ 2) / math.pi)))[-1]
	
	
		
		