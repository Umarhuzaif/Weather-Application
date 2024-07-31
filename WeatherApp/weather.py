import requests
def forecastWeather(lat,lon):
    weatherurl=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=aa89882dbadb9d5de1aa5084facbedf4'
    weatherData=requests.get(weatherurl).json()
    weatherData={
        "temperature": weatherData['main']['temp'],
        "temp_min":weatherData['main']['temp_min'],
        "temp_max":weatherData['main']['temp_max'],
        "description":weatherData['weather'][0]['description'],
        "icon":weatherData['weather'][0]['icon']
    }
    return weatherData