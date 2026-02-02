import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
import asyncio



async def main():
    """_summary_
    """
    client = MultiServerMCPClient(
        
        {
            "calculator":{
                "command":"python",
                 "args":["calculator.py"],
                  "transport":"stdio"
                 
                },
            
            
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
                
            }
            
        }
    )

    tools=await client.get_tools()
    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_agent(
        model=model,
        tools=tools
        
    )
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    
    print(response["messages"][-1].content)



asyncio.run(main())

