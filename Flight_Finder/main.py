import requests
from datetime import datetime
import os

access_token = os.getenv("AMADEUS_ACCESS_TOKEN")


def main():
    print("Welcome to the Flight Finder")

    origin = get_valid_iata_code("Enter origin location IATA code: ")
    destination = get_valid_iata_code("Enter destination location IATA code: ")
    departure_date = get_valid_date("Enter departure date (2023-08-30): ")
    return_date = get_valid_date("Enter return date (2024-10-21): ")

    while not is_return_date_after_departure(departure_date, return_date):
        print("Return date must be after the departure date.")
        return_date = get_valid_date("Enter return date (2024-10-21): ")

    adults = get_valid_passenger_number("Enter number of passengers: ")

    cheapest_price = get_cheapest_flight(origin, destination, departure_date, return_date, adults)

    if cheapest_price:
        print(f"Cheapest price found: {format_price(cheapest_price)}€")
    else:
        print("No flight found.")


def get_valid_iata_code(code):
    while True:
        iate = input(code).upper()
        if len(iate) == 3:
            return iate
        else:
            print("Invalid IATA code")


def get_valid_date(date):
    while True:
        in_date = input(date)
        if is_date_valid(in_date):
            return in_date
        else:
            print("Invalid date")


def get_valid_passenger_number(passenger):
    while True:
        try:
            number = int(input(passenger))
            if number > 0:
                return number
            else:
                print("Invalid number of passenger")
        except ValueError:
            print("Please enter a number")


def get_cheapest_flight(origin, destination, departure_date, return_date, adults):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    try:
        response = requests.get(
            url=f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={destination}&departureDate={departure_date}&returnDate={return_date}&adults={adults}",
            headers=headers)
        response.raise_for_status()
        json = response.json()
        data = json

        cheapest_price = float("inf")
        for price in data["data"]:
            try:
                total_price = float(price["price"]["total"])
                if total_price < cheapest_price:
                    cheapest_price = total_price
            except KeyError:
                continue

        return cheapest_price
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")


def format_price(price):
    return f"{price:.2f}"


def is_date_valid(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_return_date_after_departure(departure_date, return_date):
    date_departure = datetime.strptime(departure_date, "%Y-%m-%d")
    date_return = datetime.strptime(return_date, "%Y-%m-%d")
    return date_return > date_departure


if __name__ == "__main__":
    main()
