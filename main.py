#Höfundur: Huginn Þór,
class Hrutar():
	def __init__(self, nafn, thyngd, mjolk, ull, afkvaemi, laeri, frjosemi, gerd, malir):
		self.nafn = nafn
		self.thyngd = thyngd
		self.mjolk = mjolk
		self.ull = ull
		self.afkvaemi = afkvaemi
		self.laeri = laeri
		self.frjosemi = frjosemi
		self.gerd = gerd
		self.malir = malir
	def skodaNafn(self):
		return self.nafn
def hrutaSmidur(skra):
	hrutar = []
	with open(skra, "r") as f:
		lines = f.readlines()
		for x in lines:
			x = x.split(",")
			hrutur = Hrutar(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
			hrutar.append(hrutur)
		f.close
	return hrutar
	
			

