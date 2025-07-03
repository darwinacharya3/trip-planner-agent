from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper
import os
import json

class GooglePlacesSearchTool:
    def __init__(self, api_key:str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key = api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
        
    def google_search_attractions(self,place:str) -> dict:
        """
        Searches for attractions in the specified place using GooglePlaces API
        """
        return self.places_tool.run(f"top attractive places in and around {place}")
    
    def google_search_restaurants(self,place:str) -> dict:
        """
        Searches for restaurants in the specified place using GooglePlaces API
        """
        return self.places_tool.run(f"What are the top 10 restaurants and eateries in and around {place}")
    
    def google_search_activity(self,place:str) -> dict:
        """
        Searches for activities in the specified place using GooglePlaces API
        """
        return self.places_tool.run(f"What are the top 10 activities to do in and around {place}")
    
    def google_search_transportation(self,place:str) -> dict:
        """
        Searches for transportation options in the specified place using GooglePlaces API
        """
        return self.places_tool.run(f"What are the different modes of  transportation available in {place}")
    
    
class TavilyPlaceSearchTool:
    def __init__(self):
        pass
        
    def tavily_search_attraction(self,place:str) ->dict:
        """
        Searches for attractions in the specified place using Tavily API
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query" : f"top attractive places in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
        
    def tavily_search_restaurant(self,place:str) ->dict:
        """
        Searches for restaurants in the specified place using Tavily API
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query" : f"What are the top 10 restaurants and eateries in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
        
    def tavily_search_activity(self,place:str) ->dict:
        """
        Searches for activities in the specified place using Tavily API
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query" : f"What are the top 10 activities to do in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
        
    def tavily_search_transportation(self,place:str) ->dict:
        """
        Searches for transportation options in the specified place using Tavily API
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query" : f"What are the different modes of  transportation available in {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result