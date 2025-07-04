from langgraph.graph import StateGraph,MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from prompt_library.prompt import SYSTEM_PROMPT
from utils.model_loader import ModelLoader
from tools.weather_info_tool import WeatherInfoTool
from tools.currency_conversion_tool import CurrencyConversionTool
from tools.calculator_tool import CalculatorTool
from tools.place_search_tool import PlaceSearchTool





class GraphBuilder():
    def __init__(self, model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        self.tools = []
        self.weather_tool = WeatherInfoTool()
        self.currency_tool = CurrencyConversionTool()
        self.calculator_tool = CalculatorTool()
        self.place_search_tool = PlaceSearchTool()
        
        self.tools.extend([*self.weather_tool.weather_tool_list,
                           *self.currency_tool.currency_converter_tool_list,
                           *self.calculator_tool.calculator_tool_list,
                           *self.place_search_tool.place_search_tool_list])
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        
        self.graph = None
        
        self.system_prompt = SYSTEM_PROMPT
    
    def agent_function(self, state: MessagesState):
        """Main Agent Function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages" : [response]}
    
    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools = self.tools))
        
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        
        self.graph = graph_builder.compile()
        return self.graph
    
    def __call__(self):
        return self.build_graph()
    
    