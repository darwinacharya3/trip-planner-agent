import os
from utils.place_info_search import GooglePlacesSearchTool, TavilyPlaceSearchTool
from typing import List
from dotenv import load_dotenv
from langchain.tools import tool


class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.google_places_search = GooglePlacesSearchTool(api_key=self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()
        
    def _setup_tools(self) -> List:
        """Setup all tools for the place search tools"""
        
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attraction(place)
                return f"Google cannot find the details due to {e}. \n Following are the attractions of {place} : {tavily_result}"
            
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            try:
                restaurant_result = self.google_places_search.google_search_restaurants(place)
                if restaurant_result:
                    return f"Following are the restaurants of {place} as suggested by google {restaurant_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurant(place)
                return f"Google cannot find the details due to {e}. \n Following are the restaurants of {place} : {tavily_result}"
            
        @tool
        def search_activity(place:str) -> str:
            """Search activities of a place"""
            try:
                activity_result = self.google_places_search.google_search_activity(place)
                if activity_result:
                    return f"Following are the activities of {place} as suggested by google {activity_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \n Following are the activities of {place} : {tavily_result}"
            
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the transportation modes of {place} as suggested by google {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \n Following are the transportation modes of {place} : {tavily_result}"
            
        return [search_attractions, search_restaurants, search_activity, search_transportation]
        
        
       