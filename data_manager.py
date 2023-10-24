# Definirea clasei DataManager care va inregistra zborurile intr-un fisier Google Sheets

import requests

SHEETY_PRICES_ENDPOINT = "****************"

class DataManager:

    def __init__(self):
        self.destination_data = {}

# Functia citeste din fisierul Google Sheets datele zborurilor inregistrate

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
# Baza de date este updatata cu noile coduri iata

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
