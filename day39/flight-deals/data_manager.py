import requests
import os
from dotenv import load_dotenv


load_dotenv()

class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/d7c610269b62e4d1afa915d55757abfb/flightDeals/prices"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
        }
        self.data = []

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_iata(self, price):
        parameters = price
        response = requests.put(url=f"{self.url}/{price['price']['id']}", json=parameters, headers=self.headers)
        response.raise_for_status()

