import requests
def geocoding(cityname):
    geourl= f'https://api.geoapify.com/v1/geocode/search?text={cityname}&apiKey=7cab694e67fe40198c4021d4f03ef3de'
    georesponses= requests.get(geourl).json()
    try:
        lat=georesponses["features"][0]["properties"]['lat']
        lon=georesponses["features"][0]["properties"]['lon']
        cityname=georesponses['features'][0]["properties"]['name']
    except:
        return None,None,None
    return lat,lon,cityname