## Tutaj odbywają się rzeczy trochę tajemne
import requests

class User:
    def __init__(self, town) -> None:
        self.town = town

    def pogoda_z(self, town:str):

        url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{town}"
        return requests.get(url).json()


npc_1 = User(town= 'warszawa')
npc_2 = User(town= 'zamosc')

print(npc_1.town)
print(npc_2.town)

print(npc_1.pogoda_z(npc_1.town))
print(npc_2.pogoda_z(npc_2.town))

