from mcp.server.fastmcp import FastMCP


mcp=FastMCP("weather")


@mcp.tool()
async def get_weather(location:str)->str:
    """Fetches the current weather for a given location.
    
    Args:
        location (str): The location to get the weather for.
    Returns:
        str: A string describing the current weather.
    """

    return "The current weather in bangalore is rainy"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")