import random
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from serpapi import GoogleSearch
from airports import airports

def get_hotel(city, startDate):
    # Load the .env file and retrieve the API keys
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    params = {
        "engine": "google_hotels",
        "q": city,
        "check_in_date": startDate,
        "check_out_date": startDate,
        "adults": "1",
        "currency": "USD",
        "hl": "en",
        "api_key": API_KEY,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    sum = 0
    average = 0
    for property in results["properties"]:
        try:
            sum += property["rate_per_night"]["extracted_lowest"]
            average += 1
        except KeyError:
            continue

    return round(sum/average)


def create_wander(startDate, holidays, budget, cities):
    """
    :param startDate:  format "%Y-%m-%d"
    :param holidays: integer
    :param budget: integer
    :param cities: comma-separated String
    :return:
    """
    # Load the .env file and retrieve the API keys
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # Get dates of travel
    startDate = datetime.strptime(startDate, "%Y-%m-%d")
    endDate = startDate + timedelta(days=int(holidays))

    # Get cities
    cities = cities.upper().split(",")

    # Get codes from each city
    codes = []
    city_to_airport_code = {city[0]: city[2] for city in airports}
    for city in cities:
        codes.append(city_to_airport_code[city])

    file = open("my_wander.pl", "w")
    file.write("% city data\n")
    for city in cities:
        print(f'city({city.lower()}).\n')
        file.write(f'city({city.lower()}).\n')
        print(f'hotel({city.lower()}, {get_hotel(city, startDate.strftime("%Y-%m-%d"))}).\n')
        file.write(f'hotel({city.lower()}, {get_hotel(city, startDate.strftime("%Y-%m-%d"))}).\n')

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

    file.write(f'?- trip({cities[0]}, {cities[len(cities) - 1]}, {budget}, {holidays}, X, Y, Z). ')

    file.close()

    run_prolog_script()

import subprocess

def run_prolog_script():
    # Construct the shell command to modify PATH and source .bashrc before running scasp
    command = """
        export PATH=$PATH:~/.ciaoroot/v1.24.0-m1/build/bin/
        source ~/.bashrc
        scasp my_wander.pl --txt -s12
        """

    # Run the command using subprocess with a shell
    process = subprocess.Popen(
        command,
        shell=True,  # Run the command through the shell
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    # Capture the output and error (if any)
    stdout, stderr = process.communicate()

    # Check for errors
    if stderr:
        print("Error:", stderr)
    else:
        return stdout


def process_bindings():
    with open("output.txt", "r") as bindingsFile:
        bindings_input = bindingsFile.read()[9:-3].replace("[ \'Y\'", ",[ \'Y\'").replace("[ \'Z\'", ",[ \'Z\'")
        print(bindings_input)
    bindings_input = "[[ ['X', 1606], ['Y', ['prague', 'frankfurt', 'vienna', 'rome']], ['Z', [1, 2, 3, 4]] ],[ ['X', 1610], ['Y', ['prague', 'frankfurt', 'vienna', 'rome']], ['Z', [1, 2, 3, 4]] ],[ ['X', 1809], ['Y', ['prague', 'frankfurt', 'vienna', 'rome']], ['Z', [1, 2, 3, 4]] ],[ ['X', 1686], ['Y', ['prague', 'frankfurt', 'vienna', 'rome']], ['Z', [1, 2, 3, 4]] ],[ ['X', 1864], ['Y', ['prague', 'frankfurt', 'vienna', 'rome']], ['Z', [1, 2, 3, 4]] ], [] ]"

    # Replace the invalid syntax with correct Python list syntax
    bindings_input_corrected = bindings_input.replace("][", "],[")

    # Use ast.literal_eval to safely evaluate the string as a Python list
    import ast

    bindings = ast.literal_eval(bindings_input_corrected)

    # Function to parse the given structure into the desired format
    def parse_bindings(bindings):
        result = []
        for binding in bindings:
            if binding:  # Skip empty lists
                parsed_entry = {}
                for item in binding:
                    if item[0] == 'X':
                        parsed_entry['PRICE'] = item[1]
                    elif item[0] == 'Y':
                        parsed_entry['VISITS'] = item[1]
                    elif item[0] == 'Z':
                        parsed_entry['DAYS'] = item[1]
                result.append(parsed_entry)
        return result

    # Call the function
    parsed_data = parse_bindings(bindings)
    print(parsed_data)

    os.remove("output.txt")

    return parsed_data


# FLASK implementation
from flask import Flask, jsonify, request

app = Flask(__name__)

from flask_cors import CORS
CORS(app)  # Enable CORS for all routes

@app.route('/api/run-script', methods=['GET'])
def run_script():
    try:
        date = request.args.get('date')  # Get the argument from the URL query string
        length = int(request.args.get('length'))
        budget = int(request.args.get('budget'))
        cities = request.args.get('cities')
    except:
        date = "2025-01-20"  # hard-coded
        length = "5" # hard-coded
        budget = "200000" # hard-coded
        cities = "prague,frankfurt,vienna,rome" # hard-coded
    print(date, length, budget, cities)

    # create_wander(date, length, budget, cities) # Runs API
    run_prolog_script()
    data = process_bindings()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)