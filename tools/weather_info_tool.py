
import os
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv
from utils.weather_info import WeatherForeCastTool

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForeCastTool(api_key=self.api_key)
        self.weather_tool_list = self._setup_tools()
        
    def _setup_tools(self) -> List:
        """Setup all tools for weather forecast tool"""
        @tool
        def get_current_weather(city:str) -> str:
            """Get current weather for a city"""
            weather_data = self.weather_service.get_current_weather(place=city)
            if weather_data:
                temp = weather_data.get("main", {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"Current weather in {city} : {temp} degree C, {desc}"
            return f"Could not fetch weather for {city}"
        
        @tool
        def get_forecast_weather(city:str)->str:
            """Get weather forecast fr a city"""
            forecast_data = self.weather_service.get_forcast_weather(place=city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp}°C, {desc}")
                return f"Weather forecast for {city}: \n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {city}"
        
        return [get_current_weather, get_forecast_weather]
                
            