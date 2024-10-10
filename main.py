#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import time
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
flight_data = FlightData
ORIGING_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"]=="":
        row["iataCode"]=flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    flights = flight_search.check_flights(
        ORIGING_CITY_IATA,destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price fight found to {destination['city']}!")
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only ${cheapest_flight.price} to fly "
                        f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                        f"on {cheapest_flight.out_date} until {cheapest_flight.return_data}."
        )