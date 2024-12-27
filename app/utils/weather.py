import requests
from dotenv import load_dotenv
import os
import openai

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


openai.api_key = os.getenv("OPEN_AI_KEY")

base_url = "http://api.weatherapi.com/v1"


def fetch_weather(city_name):
    try:
        complete_url = f"{base_url}/current.json?key={WEATHER_API_KEY}&q={city_name}"
        response = requests.get(complete_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def generate_weather_summary(city_name):
    weather_data = fetch_weather(city_name)
    if weather_data:
        location = weather_data["location"]["name"]
        region = weather_data["location"]["region"]
        country = weather_data["location"]["country"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        prompt = f"""
        The current weather in {location}, {region}, {country} is {temperature}°C with {condition}.
        If the user asks whether it is sunny, just answer 'Yes' or 'No'.
        If the user asks about the temperature, provide the temperature in °C.
        If the user asks about the weather condition, describe it (e.g., sunny, cloudy, etc.).
        Make sure to tailor your responses to the question asked, and avoid giving unnecessary information.
        """
      
        return prompt

    return None


def get_openAI_weather_response(city_name):
    prompt = generate_weather_summary(city_name)
    messages = [{"role": "user", "content": prompt}]
    if prompt:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o", messages=messages, max_tokens=150, temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except openai.error.OpenAIError as e:
            print(f"Error with GPT-4 request: {e}")
            return "Sorry, I couldn't generate a response."
    return "Sorry, there was an issue with the weather data."
