from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights


# res = tavily_search("Best hotels in Andhra Pradesh, India")
# print(res)

res = search_flights("Plan a 7 days Nepal trip from Bangladesh")
print(res)


# load_dotenv()

# print("API Key Loaded:", bool(os.getenv("TAVILY_API_KEY")))

