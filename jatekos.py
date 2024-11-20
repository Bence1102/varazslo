import random
class Jatekos:
    def __init__(self,nev:str="Jatekos",poz:int=0,kaszt:str="harcos",emo:str="H"):
        self.nev=nev
        self.hp=3+random.randint(1,6)
        self.kaszt=kaszt
        self.poz=poz
        self.emo=emo

    '''modosítja a pozíciojat mindenkörben ez a metodus.'''    
    def set_pozicio(self):
        self.poz=random.randint(0,2)

    def set_hp(self):
        self.hp=self.hp-random.randint(0,2)



    def __str__(self):
        return f"Név: {self.nev} Kaszt: {self.kaszt} HP: {self.hp} Pozíció: {self.poz} Karakter: {self.emo}"
    
