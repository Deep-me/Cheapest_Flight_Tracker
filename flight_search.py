import requests
from datetime import datetime

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = "[YOUR API KEY]"
        self.api_secret = "[YOUR API SECRET]"
        self.token = self.get_new_token()

    def get_new_token(self):
        header = {
            'content-type':'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type' : 'client_credentials',
            'client_id' : self.api_key,
            'client_secret' : self.api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT,headers = header,data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self,city_name):

        print(f"Using this token to get destination {self.token}")
        headers = {"Authorization" :f"Bearer {self.token}"}
        query = {
            "keyword":city_name,
            "max":"2",
            "include":"AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT,headers = headers,params=query)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers = {"Authorization" : f"Bearer {self.token}"}
        query = {
            "originLocationCode":origin_city_code,
            "destinationLocationCode":destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate":to_time.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop":"true",
            "currencyCode":"GBP",
            "max":"10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT,headers=headers,params=query)
        if response.status_code != 200:
            print(f"check_flight() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentaion:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference")
            print("Response body:",response.text)
            return None
        print(response.json())
        return  response.json()