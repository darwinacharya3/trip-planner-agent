
import requests

class WeatherForeCastTool:
    def __init__(self, api_key : str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        
    def get_current_weather(self,place:str):
        """Get current weather of a place"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q" : place,
                "appid" : self.api_key,
            }
            response = requests.get(url,params=params)
            return response.json() if response.status_code == 200 else {"error": "Failed to fetch weather data"}
        except Exception as e:
            raise e
        
        def get_forcast_weather(self,place:str):
            """Get weather forecast of a place"""
            try:
                url = f"{self.base_url}/forecast"
                params = {
                    "q": place,
                    "appid": self.api_key,
                    "cnt" : 10,  # Number of forecasted days
                    "units": "metric"  # Use metric units for temperature
                }
                
                response = requests.get(url,params=params)
                return response.json() if response.status_code == 200 else {"error": "Failed to fetch weather data"}
            except Exception as e:
                raise e