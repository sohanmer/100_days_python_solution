from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import time


ORIGIN_CITY_IATA = "LON"
data_manager = DataManager()
flight_search = FlightSearch()
data = data_manager.get_data()
notification_manager = NotificationManager()

try:
    city_data = data['prices']
    price = {}
    for dest in city_data:
        if dest['iataCode'] == '':
            iata = flight_search.city_search(dest['city'])
            print(iata)
            price['price'] = {
                "id": dest['id'],
                "city": dest['city'],
                "iataCode": iata,
                "lowestPrice": dest['lowestPrice']
            }

        data_manager.update_iata(price)
except KeyError:
    print("No data returned from the request")


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

try:
    for destination in city_data:
        print(f"Getting flights for {destination['city']}...")
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        cheapest_flight = find_cheapest_flight(flights)
        print(f"{destination['city']}: £{cheapest_flight.price}")
        # Slowing down requests to avoid rate limit
        time.sleep(2)
        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            print(f"Lower price flight found to {destination['city']}!")
            notification_manager.send_sms(
                message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                             f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                             f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
except KeyError:
    print("No data returned from the request")

