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
                if val == "1":
                        return self.thyngd
                elif val == "2":
                        return self.mjolk
                elif val == "3":
                        return self.ull
                elif val == "4":
                        return self.afkvaemi
                elif val == "5":
                        return self.laeri
                elif val == "6":
                        return self.frjosemi
                elif val == "7":
                        return self.gerd
                elif val == "8":
                        return self.malir
def hrutaSmidur(skra):  #Býr til alla hrútana sem object
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
def skipta(listi):      #Skiptir öllum hrúta objectunum í tvo lista, eg og talva
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
def skiptaSpilum(listix, listiy):       #Tekur fremsta spilið ú lista-x og færir það í lista-y
        listiy.append(listix[0])
        listiy.append(listiy[0])
        listiy.remove(listiy[0])
        listix.remove(listix[0])
def jafntefli(listix, listiy):
        listix.remove(listix[0])
        listiy.remove(listiy[0])
def compare(ob1, ob2, val):
        if ob1.val(val) > ob2.val(val):
                return 1
        elif ob2.val(val) > ob1.val(val):
                return 0
        else:
                return None
def spilad(ob1, ob2, val, ob1list, ob2list, templisti):
        utkoma = compare(ob1, ob2, val)
        if utkoma == 1:
                print("Spilari eitt vann umferðina")
                skiptaSpilum(ob2list, ob1list)
                if len(templisti) != 0:
                        ob1list.append(templisti[0])
                        ob1list.append(templisti[1])
                        templisti.remove(templisti[0])
                        templisti.remove(templisti[0])
                print("Spilari 1: {}\nSpilari 2: {}\nGeymd Spil: {}".format(len(ob1list), len(ob2list), len(templisti)))
                        
                
        elif utkoma == 0:
                print("Leikmaður tvö vann umferðina")
                skiptaSpilum(ob1list, ob2list)
                if len(templisti) != 0:
                        ob2list.append(templisti[0])
                        ob2list.append(templisti[1])
                        templisti.remove(templisti[0])
                        templisti.remove(templisti[0])
                print("Spilari 1: {}\nSpilari 2: {}\nGeymd Spil: {}".format(len(ob1list), len(ob2list), len(templisti)))
        else:
                print("Jafntefli")
                templisti.append(ob1list[0])
                templisti.append(ob2list[0])
                jafntefli(ob1list, ob2list)
                if len(templisti) == 0:
                        print("Spilari 1:{}\nSpilari 2:{}".format(len(ob1list), len(ob2list)))
                elif len(templisti) != 0:
                        print("Spilari 1: {}\nSpilari 2: {}\nGeymd Spil: {}".format(len(ob1list), len(ob2list), len(templisti)))

def sigurcheck(listi1, listi2):
        if len(listi1) == 0:
                return 1
        elif len(listi2) == 0:
                return 0

        
def leikur(eg, talva):
        spila = 0
        listi = []
        while True:
                if sigurcheck(eg, talva) == 1:
                        print("\nSpilari tvö vann leikinn!")
                        break
                elif sigurcheck(eg, talva) == 0:
                        print("\nSpilari eitt vann leikinn!")
                        break
                print("--------------------------------")
                if spila == 0:
                        obj1 = eg[0]
                        obj2 = talva[0]
                        obj1.skodaNafn()
                        obj1.skodaEiginleika()
                        val = input("veldu eiginleika: ")
                        print("\n")
                        leyfinlegtval = ["1","2","3","4","5","6","7","8"]
                        if val in leyfinlegtval:
                                print(obj1.val(val))
                                print(obj2.val(val))
                                print("Leikmaður eitt velur að keppa í {}. lið.\n".format(val))
                                spilad(obj1, obj2, val, eg, talva, listi)
                        else:
                                print("ekkert valið, veldu aftur")
                        spila = 1
                else:                   #talva
                        obj1 = eg[0]
                        obj2 = talva[0]
                        spila = 0
                        val = str(random.randint(1,8))
                        print("Leikmaður tvö velur að keppa í {}. lið.\n".format(val))
                        spilad(obj1, obj2, val, eg, talva, listi)

def multiplayer(eg, talva):
        spila = 0
        listi = []
        while True:
                if sigurcheck(eg, talva) == 1:
                        print("\nSpilari tvö vann leikinn!")
                        break
                elif sigurcheck(eg, talva) == 0:
                        print("\nSpilari eitt vann leikinn!")
                        break
                print("--------------------------------")
                if spila == 0:
                        obj1 = eg[0]
                        obj2 = talva[0]
                        obj1.skodaNafn()
                        obj1.skodaEiginleika()
                        val = input("veldu eiginleika: ")
                        print("\n")
                        leyfinlegtval = ["1","2","3","4","5","6","7","8"]
                        if val in leyfinlegtval:
                                print(obj1.val(val))
                                print(obj2.val(val))
                                print("Leikmaður eitt velur að keppa í {}. lið.\n".format(val))
                                spilad(obj1, obj2, val, eg, talva, listi)
                        else:
                                print("ekkert valið, veldu aftur")
                        spila = 1
                else:                   #leikmaður 2
                        obj1 = eg[0]
                        obj2 = talva[0]
                        obj1.skodaNafn()
                        obj1.skodaEiginleika()
                        val = input("veldu eiginleika: ")
                        print("\n")
                        leyfinlegtval = ["1","2","3","4","5","6","7","8"]
                        if val in leyfinlegtval:
                                print(obj1.val(val))
                                print(obj2.val(val))
                                print("Leikmaður tvö velur að keppa í {}. lið.\n".format(val))
                                spilad(obj1, obj2, val, eg, talva, listi)
                        else:
                                print("ekkert valið, veldu aftur")
                        spila = 0
def main():
        while True:
                valmynd = input("Viltu spila:\n1. Einn á móti tölvu\n2. Með öðrum leikmanni á sömu tölvu\n3. Hætta við\n: ")
                if valmynd == "1":
                        leikur(eg, talva)
                elif valmynd == "2":
                        multiplayer(eg, talva)
                elif valmynd == "3":
                        print("Thanks anyway...")
                        break
                else:
                        print("Veldu 1-3")
                

eg = hrutaSmidur("hrutar.txt")
talva = skipta(eg)
main()
