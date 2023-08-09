class Vault:
    def __init__(self, gold=0,silver=0,bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    def __str__(self):
        return f'{self.gold}, {self.silver}, {self.bronze}'
    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        bronze = self.bronze + other.bronze
        return Vault(gold,silver,bronze)

potter = Vault(100,20,30)
weasley = Vault(200.20,30)

print(potter)
print(weasley)

total = potter + weasley
print(total)