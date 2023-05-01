from db import pg
from datetime import datetime, timedelta, date
import requests
import json
import re
import pandas as pd
import numpy as np

def analyise_soil():
    soilData = []
    conn = pg.connect()
    deltaTime = datetime.now() - timedelta(hours=24)
    #print(deltaTime,)
    querry = "SELECT \"i2cStore\" FROM \"i2cData\" WHERE DATE_TRUNC('hour',timestamp) >= %s;"
    params = (deltaTime,)
    result = pg.execute_query(conn,querry,params)
    for row in result:
        json_data = json.loads(re.sub(r"\'","\"", str(row[0])))
        i2cdata = json_data['I2C']
        for data in i2cdata:
            soilData.append({'address': int(data['address']), 'Soil humid': [int(data['Soil humid'])]})
    merged_data = {}
    for item in soilData:
        key = item['address']
        if key in merged_data:
            merged_data[key]['Soil humid'] += item['Soil humid']
        else:
            merged_data[key] = item
    merged_list = [value for key, value in merged_data.items()]
    df = pd.DataFrame(merged_list)
    df['std'] = df['Soil humid'].apply(lambda x: np.std(x))

    addresses = df.loc[df['std'] > 6, 'address'].tolist()
    return addresses


def light(location):
    # Get latitude and longitude of location
    lat, lon = get_lat_lon(location)

    # Get current date and time
    now = datetime.now()

    # Calculate day length
    day_length, sunrise, sunset = get_day_length(lat, lon, now, location)

    # Check if day length is long enough
    if day_length >= 10: # change this value to the minimum number of hours of sunlight required for your plants
        return (True , sunrise, sunset)
    else:
        return (False , sunrise, sunset)

def get_lat_lon(location):
    # Use geocoding API to get latitude and longitude of location
    url = f"https://nominatim.openstreetmap.org/search/{location}?format=json"
    response = requests.get(url).json()
    lat = float(response[0]['lat'])
    lon = float(response[0]['lon'])
    return lat, lon

def get_day_length(lat, lon, date_time, location):
    # Use sunrise-sunset API to get day length
    date = date_time.date().strftime('%m/%d/%Y')
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&date={date}"
    response = requests.get(url).json()
    sunrise = datetime.strptime(response['results']['sunrise'], '%I:%M:%S %p').time()
    sunset = datetime.strptime(response['results']['sunset'], '%I:%M:%S %p').time()
    day_length = 10
    return day_length, sunrise, sunset
