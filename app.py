from flask import Flask
from flask import jsonify
import requests
from datetime import datetime
app = Flask(__name__)

def weatherAPI(city, country):
    """
    Gets the current weather conditions for a given city and country using the weatherapi.com API.
    
    Parameters:
        city (str): The name of the city.
        country (str): The name of the country.
    
    Returns:
        A dictionary representing the current weather conditions for the given location.
    """
    # Enter your API key here
    api_key = "1519edbf82994ba980874948231502"
    
    # Send a request to the weatherapi.com API to get the current weather conditions
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}")
    
    # Check if the request was successful and the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response into a dictionary and return it
        return response.json()
    else:
        # If the request was not successful, print an error message and return None
        print(f"Error getting weather data: {response.status_code}")
        return None


@app.route('/')
def hello():
    print("I am an Automatic weather report Machine")
    return 'Hello Automatic weather report Machine! Please use it to get the weather report at route by typing: /weather/city/country'

@app.route('/weather/<city>/<country>')
def changeroute(city, country):
    print(f"Get weather report for city:{city} and country:{country}")
    result = weatherAPI(heads, legs)
    return result
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
