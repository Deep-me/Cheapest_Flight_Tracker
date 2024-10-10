import requests
from requests.auth import HTTPBasicAuth

SHEET_ENDPOINT = "https://api.sheety.co/72d8417c8596cab4dab013de0c8f999c/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = "[YOUR USER NAME]"
        self.password = "[YOUR PASSWORD]"
        self.authorization = HTTPBasicAuth(self.user,self.password)
        self.destination_data = {}
        self.headers_sheety = {"Authorization":"[YOUR TOKEN AUTH]"}
    def get_destination_data(self):
        response = requests.get(SHEET_ENDPOINT,auth=(self.user,self.password),headers=self.headers_sheety)
        data = response.json()
        self.destination_data = data["prices"]
        return  self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}",json=new_data,
                            auth=(self.user,self.password),headers=self.headers_sheety)
            print(response.text)