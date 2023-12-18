import requests


class User:
    def __init__(self, town) -> None:
        self.town = town

    def pogoda_z(self, town:str):

        url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{town}"
        return requests.get(url).json()
