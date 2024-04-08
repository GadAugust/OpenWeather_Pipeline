import pandas as pd
import requests




def extract_data(file, api_key):
    '''
    This is a function to extract current weather conditions of cities
    from all locations on a file from the openweathermap API.
    The contains longitude and latitudes

    parameters:
    - file - an xlsx file
    - api_key - openweathermap api key
    Return values: a pandas dataFrame object
    Return Type: a pandas dataFrame
    '''
    df = pd.read_excel(file)

    #initialize an empty list to hold the rows
    rows = []

    for index, row in df.iterrows():
        lat = row['lat']
        lon = row['lng']

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        response = requests.get(url)
        data = response.json()   

        condition = (data['weather'][0]['description'])
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        lats = data['coord']['lat']
        lons =data['coord']['lon'] #lons.append(data['coord']['lon'])
        humidity = data['main']['humidity']


        city = data['name']
        unix_date = data['dt']
        timezones = data['timezone']

        rows.append((city, lats, lons, condition, temp, humidity, wind_speed, unix_date, timezones))
        
    weather_df = pd.DataFrame(rows, columns = ['city','latitude', 'longitude', 'condition',
                                               'temp','humidity','wind_speed','unix_date', 'unix_timezone'])
    return weather_df