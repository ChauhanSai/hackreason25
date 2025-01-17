import random
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from json import loads
from serpapi import GoogleSearch

from backend.airports import airports

# Load the .env file
load_dotenv()

# Retrieve the API keys
API_KEY = os.getenv("API_KEY")

# Get dates of travel
#startDate = input("Start Date (YYYY-MM-DD): ")
startDate = "2025-01-20"
startDate = datetime.strptime(startDate, "%Y-%m-%d")
#holidays = input("Length of trip (days): ")
holidays = "5"
endDate = startDate + timedelta(days=int(holidays))

# Get cities
# cities = input("Comma-separated list of cities: ")
cities = "prague,frankfurt,vienna,rome"
cities = cities.upper().split(",")

# Get codes from each city
codes = []
city_to_airport_code = {city[0]: city[2] for city in airports}
for city in cities:
    codes.append(city_to_airport_code[city])

file = open("my-wander.pl", "w")
file.write("% city data\n")
for city in cities:
    print(f'city({city.lower()}).\n')
    file.write(f'city({city.lower()}).\n')
    print(f'hotel({city.lower()}, {random.randint(40, 200)}).\n')
    file.write(f'hotel({city.lower()}, {random.randint(40, 200)}).\n')

file.write("\n")

print(codes)
print(f'Starting trip on {startDate} for {holidays} days. Must travel to {cities} with codes {codes}.')

# All pairs of cities
codePairs = []
cityPairs = []
for i in range(len(codes)):
    for j in range(len(codes)):
        if i != j:
            codePairs.append([codes[i], codes[j]])
            cityPairs.append([cities[i], cities[j]])

print(codePairs)
print(cityPairs)

file.write("% route data\n")
for i in range(len(codePairs)):
    currentDate = startDate
    currentDay = 1
    while currentDate < endDate:
        print(codePairs[i], currentDate.strftime("%Y-%m-%d"), "(" + str(currentDay) + ")")
        print(codePairs[i][0])
        print(codePairs[i][1])

        # Scrape data
        params = {
            "engine": "google_flights",
            "departure_id": codePairs[i][0],
            "arrival_id": codePairs[i][1],
            "outbound_date": currentDate.strftime("%Y-%m-%d"),
            "currency": "USD",
            "hl": "en",
            "api_key": API_KEY,
            "type": 2
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        # print(results)

        for flights in results["best_flights"]:
            print(f'route({cityPairs[i][0].lower()},{cityPairs[i][1].lower()},{flights["price"]},{currentDay}).\n')
            file.write(f'route({cityPairs[i][0].lower()},{cityPairs[i][1].lower()},{flights["price"]},{currentDay}).\n')

        for flights in results["other_flights"]:
            print(f'route({cityPairs[i][0].lower()},{cityPairs[i][1].lower()},{flights["price"]},{currentDay}).\n')
            file.write(f'route({cityPairs[i][0].lower()},{cityPairs[i][1].lower()},{flights["price"]},{currentDay}).\n')

        # Iterate by one day
        currentDate = currentDate + timedelta(days=1)
        currentDay += 1

with open("wander.pl.example", "r") as copyFile:
    for line in copyFile:
        file.write(line)

file.write(f'?- trip({cities[0]}, {cities[len(cities) - 1]}, 200000, {holidays}, X, Y, Z). ')

file.close()