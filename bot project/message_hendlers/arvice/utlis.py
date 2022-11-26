import aiohttp
Api_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "91cf925583bbcbce7111a754e2e864b8"



async def get_weather():
    async with aiohttp.ClientSession() as session:
        r= await session.get(Api_URL+"?q=London&appid={WEATHER_API_KEY}")
        print(r.content)

get_weather()
