from DiamondTrap import King
from S1E7 import Baratheon, Lannister
from S1E9 import Character


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.eyes = "blue"
Joffrey.hairs = "light"
print(Joffrey.eyes)
print(Joffrey.hairs)
print(Joffrey.__dict__)
if (
    isinstance(Joffrey, King)
    and issubclass(King, Character)
    and issubclass(King, Lannister)
    and issubclass(King, Baratheon)
):
    print("OK")
