from flask import Flask,request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def apps():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        # Give city name
        city_name = request.form.get('city')

        api_key = "d7d545f7a4d3b748645fce10812fad78"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"


        # complete_url variable to store``
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":
            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]
            abc = 459.67
            current_temperature = current_temperature - abc

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidiy = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            return ''' <h3> City : {} </h3>
                       <h3> Temperature (in kelvin unit): {} </h3>
                       <h3> Atmospheric pressure (in hPa unit): {} </h3>
                       <h3> Humidity (in percentage): {} </h3>
                       <h3> Description : {} </h3>
                       <input type="submit" value="Back"><br><br>'''.format(city_name, current_temperature, current_pressure,
                                                             current_humidiy, weather_description)

        else:
            return ''' <h3> Invalid City </h3>'''
       
    return '''<form method="POST">
                      City <input type="text" name="city"><br><br>
                      <input type="submit" value="Submit"><br><br>
                  </form>'''

if __name__ == "__main__":
    app.run(debug=True)