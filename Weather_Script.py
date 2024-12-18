import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city_name}")
        print(f"Temperature: {main['temp']}K")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "f8378c48b30542d1244982c1f6049d4f"
    get_weather(city_name, api_key)