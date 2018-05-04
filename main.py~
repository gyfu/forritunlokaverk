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
<<<<<<< HEAD
        def skodaThyngd(self):
                print(self.thyngd)
        def keppa(self, other, val):
                if self.val > other.val:
                        return True
                elif self.val < other.val:
                        return False
                else: 
                        return 2
=======
        def skodaEiginleika(self):
                print("\n    1. Þyngd(kg):          ", self.thyngd)
                print("    2. Mjólklagni dætra:   ", self.mjolk)
                print("    3. Einkunn ullar:      ", self.ull)
                print("    4. Fjöldi afkvæma:     ", self.afkvaemi)
                print("    5. Einkunn læris:      ", self.laeri)
                print("    6. Frjósemi:           ", self.frjosemi)
                print("    7. Gerð/þykkt bakvöðva:", self.gerd)
                print("    8. Einkunn fyrir malir:", self.malir)
                print("--------------------------------")
        def val(self, val):
                if val == 1:
                        return self.thyngd
                elif val == 2:
                        return self.mjolk
                elif val == 3:
                        return self.ull
                elif val == 4:
                        return self.afkvaemi
                elif val == 5:
                        return self.laeri
                elif val == 6:
                        return self.frjosemi
                elif val == 7:
                        return self.gerd
                elif val == 8:
                        return self.malir
        
>>>>>>> fe9060634b219f0c901a64d8a0f70243f0bcb31d
        
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

def leikur(eg, talva):
        spila = 0
        teljari = -1
        obj1 = eg[0]
        obj2 = talva[0]
        while True:
                print("--------------------------------")
                if spila == 0:        #eg
                        teljari += 1
                        obj1.skodaNafn()
                        obj1.skodaEiginleika()
                        val = int(input("veldu eiginleika: "))
                        print("\n")

                        if val > 0 and val < 9:
                                print(obj1.val(val))
                                print(obj2.val(val))
                                if val == 1:
                                        print("þyngd")
                                elif val == 2:
                                        print("mjolk")
                                elif val == 3:
                                        print("ull")
                                elif val == 4:
                                        print("fjoldi")
                                elif val == 5:
                                        print("laeri")
                                elif val == 6:
                                        print("frjosemi")
                                elif val == 7:
                                        print("bak")
                                elif val == 8:
                                        print("malir") #kveikur er op
                                        
                                if obj1.val(val) > obj2.val(val):
                                        print("eg fæ stigið")
                                elif obj1.val(val) < obj2.val(val):
                                        print("talvan fær stigið")
                                else:
                                        print("jafntefli")
                        else:
                                print("ekkert valið, veldu aftur")
                        spila = 1

                        
                else:                   #talva
                        
                        spila = 0


eg = hrutaSmidur("hrutar.txt")
#hrutur = eg[0]
#hrutur.skodaNafn()
talva = skipta(eg)
eg[0].skodaThyngd()
talva[0].skodaThyngd()



<<<<<<< HEAD

#leikur(talva)
#print("\nhin spilin\n")
#print(eg)
=======
print(talva)
print("\nhin spilin\n")
print(eg)
>>>>>>> fe9060634b219f0c901a64d8a0f70243f0bcb31d

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

print("\nleikur\n")
leikur(eg, talva)






















        
