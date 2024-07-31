from flask import Flask,render_template,request

from geocoding import geocoding
from weather import forecastWeather
from kelvinTocelcius import Tocelcius

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        cityname=request.form['search']
        try:
            lat,lon,cityname=geocoding(cityname)
            if lat==None and lon==None:
                return render_template('index.html',error=True)
        except Exception as e:
            
            return f'Oops{e}'
    #Gets the Coordinates of given City name.
        weatherdata=forecastWeather(lat,lon)
    #gets The Weather Forecast Of given City by its coordinates.
        weatherdata=Tocelcius(weatherdata)
        return render_template('index.html',output=True,weatherData=weatherdata,cityname=cityname)
    return render_template('index.html',output=False)

if __name__=='__main__':
    app.run(debug=True)