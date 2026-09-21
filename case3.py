class HeroGame:
    def __init__(self, nama, role, damage):
        self.nama = nama
        self.role = role
        self.damage = damage
        self.hp = 100

    def serang(self, musuh):
        musuh.hp -= self.damage
        print(f"⚔️ {self.nama} ({self.role}) menyerang {musuh.nama} sebesar {self.damage} DMG!")
        print(f"🛡️ HP {musuh.nama} tersisa: {musuh.hp}\n")
        
    def heal(self):
        self.hp += 15
        print(f"✨ {self.nama} menggunakan heal! HP bertambah 15.") #{self,}
        print(f"🛡️ HP {self.nama} saat ini: {self.hp}\n")    

hero1 = HeroGame("Chandra", "Mage", 25)
hero2 = HeroGame("Gaby", "Assassin", 35)

print(f"⚔️ Start: {hero1.nama} (HP:{hero1.hp}) vs {hero2.nama} (HP:{hero2.hp})\n")
hero1.serang(hero2)
hero2.serang(hero1)      

hero1.heal()