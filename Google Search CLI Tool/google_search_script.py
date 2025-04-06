import requests
import sys

def google_search(query, num_results=5):
    api_key = "651cd4067083dba69a61fee953b51f916f1d7036c480af9948fb7039b10b74ea"  # Replace with your SerpAPI key
    search_url = "https://serpapi.com/search"

    params = {
        "q": query,
        "api_key": api_key,
        "num": num_results
    }

    response = requests.get(search_url, params=params)
    data = response.json()

    if "organic_results" in data:
        print(f"\n🔍 Top {num_results} Google Search Results for: {query}\n")
        for index, result in enumerate(data["organic_results"][:num_results], start=1):
            print(f"{index}. {result['title']}")
            print(f"   🔗 {result['link']}\n")
    else:
        print("⚠️ No results found or API limit reached.")

# Check if a search query was provided as a command-line argument
if len(sys.argv) > 1:
    search_query = " ".join(sys.argv[1:])
else:
    search_query = input("Enter your search query: ")

google_search(search_query)
