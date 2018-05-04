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
        def skodaThyngd(self):
                print(self.thyngd)
        def keppa(self, other, val):
                if self.val > other.val:
                        return True
                elif self.val < other.val:
                        return False
                else: 
                        return 2
        
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

def keppa(obj1, obj2, val):
        if obj1.val > obj2.val:
                return True
        elif obj1.val < obj2.val:
                return False
        else: 
                print("Jafntefli")
                return 2

def leikur(badir):
        print(badir)


eg = hrutaSmidur("hrutar.txt")
#hrutur = eg[0]
#hrutur.skodaNafn()
talva = skipta(eg)
eg[0].skodaThyngd()
talva[0].skodaThyngd()




#leikur(talva)
#print("\nhin spilin\n")
#print(eg)

############################################### skoda spilin i hvorum lista
#teljari = -1
#for x in eg:
#        teljari += 1
#        eg[teljari].skodaNafn()

#print("\nhin spilin\n")
#teljari = -1
#for x in talva:
#        teljari += 1
#        talva[teljari].skodaNafn()
############################################### skoda spilin i hvorum lista











        
