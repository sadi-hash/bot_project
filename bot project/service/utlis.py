
from datetime import datetime
import aiohttp
import asyncio

API_URL = "https://api.openweathermap.org/data/2.5/weather"     
WEATHER_API_KEY = "91cf925583bbcbce7111a754e2e864b8"

#"91cf925583bbcbce7111a754e2e864b8"
def convert_unix_to_time(unix_time):
    time = datetime.fromtimestamp(unix_time)
    return time.strftime("%m-%d %H:%M")

async def get_weather(city_name):
    async with aiohttp.ClientSession() as session:
         async with session.get(API_URL+f"?q={city_name}&appid={WEATHER_API_KEY}") as r:
            data = await r.json()
            
            weather_data = {
                "temp":round (data["main"]["temp"] - 273),
                "feels_like":round (data["main"]["feels_like"]-273),
                "pressure": data ["main"]["pressure"],
                "humidity": data ["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "city_time":convert_unix_to_time(data["dt"]),
                "sunset"    :convert_unix_to_time(data["sys"]["sunset"]),
                "sunrise":convert_unix_to_time(data["sys"]["sunrise"])
            }
            print(weather_data)
            
            return  weather_data
            
 
            









