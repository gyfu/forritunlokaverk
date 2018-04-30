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

        talva = []

        for x in listi:
                teljari += 1
                if teljari %2 == 0:
                        talva.append(x)
        for i in listi:
                if i in talva:
                        listi.remove(i)

        return talva
        

def leikur(badir):
        print(badir)


eg = hrutaSmidur("hrutaspil.txt")
hrutur = eg[0]
hrutur.skodaNafn()

talva = skipta(eg)


leikur(talva)
print("\nhin spilin\n")
print(eg)

############################################### skoda spilin i hvorum lista
teljari = -1
for x in eg:
        teljari += 1
        eg[teljari].skodaNafn()

print("\nhin spilin\n")
teljari = -1
for x in talva:
        teljari += 1
        talva[teljari].skodaNafn()
############################################### skoda spilin i hvorum lista












