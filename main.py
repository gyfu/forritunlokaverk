#Höfundur: Huginn Þór,Jakub Ingvar
import random
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
		print(self.nafn)
        
def hrutaSmidur(skra):
	hrutar = []
	with open(skra, "r") as f:
		lines = f.readlines()
		for x in lines:
			x = x.split(",")
			hrutur = Hrutar(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
			hrutar.append(hrutur)
		f.close
	random.shuffle(hrutar)	
	return hrutar
    
def skipta(listi):
    teljari = 0
    eg = []
    talva = []
    badir = []
    for x in listi:
        teljari += 1
        if teljari %2 == 0:
            talva.append(x)
        else:
            eg.append(x)
    badir.append(eg)
    badir.append(talva)
    return badir
        

hrutar = hrutaSmidur("hrutaspil.txt")
hrutur = hrutar[0]
hrutur.skodaNafn()

badir = skipta(hrutar)
print(badir)


