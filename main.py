
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from utils.save_to_document import save_document
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
import os
from dotenv import load_dotenv
from IPython.display import display, Image

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class QueryRequest(BaseModel):
    question: str
    
@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider = "groq")
        
        react_app = graph()
        
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)
            
        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        # Assuming request is a pydantic object like {"question" : "your text"}
        messages = {"messages" : [query.question]}
        
        output = react_app.invoke(messages)
        
        # If result is dict with messages:
        if isinstance(output, dict) and  "messages" in output:
            final_output = output["messages"][-1].content # last  AI response
        else:
            final_output = str(output)
            
        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)