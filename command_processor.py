# command_processor.py

import datetime
import webbrowser
import pyjokes
import requests
import time
from config import OPENWEATHER_API_KEY

# Function to process the recognized command and perform corresponding actions
def process_command(command):
    if "what time is it" in command:
        # Get the current time
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    
    elif "search for" in command:
        # Extract the query to search for
        query = command.replace("search for", "").strip()
        # Open the default web browser with the search query
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}..."
    
    elif "tell me a joke" in command:
        # Get a random joke using pyjokes
        joke = pyjokes.get_joke()
        return joke
    
    elif "what's the weather like" in command:
        # Fetch weather data from OpenWeatherMap API
        return get_weather_info()
    
    elif "set a timer for" in command:
        # Extract the timer duration from the command
        try:
            seconds = int(command.split("set a timer for")[-1].strip().split()[0])
            # Set a timer and notify when it finishes
            time.sleep(seconds)
            return f"Timer for {seconds} seconds is up!"
        except ValueError:
            return "Sorry, I couldn't understand the timer duration."

    else:
        return "Sorry, I didn't catch that. Please try again."

# Function to fetch weather information using OpenWeatherMap API
def get_weather_info():
    try:
        # Make a request to OpenWeatherMap API
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={OPENWEATHER_API_KEY}&units=metric")
        weather_data = response.json()
        
        if weather_data["cod"] == 200:
            # Extract the relevant weather info
            weather_description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            return f"The current weather is {weather_description} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather information."
    
    except Exception as e:
        return f"An error occurred: {e}"
