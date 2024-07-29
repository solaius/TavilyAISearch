import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the Tavily API key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TAVILY_API_ENDPOINT = os.getenv("TAVILY_API_ENDPOINT")

def search_tavily(query, top_k=5):
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": top_k,
        "search_depth": "basic",
        "include_answer": True,  # Include the answer in the results
        "include_images": True,  # Include images in the results
        "include_raw_content": True,  # Include raw content in the results
        "include_domains": [],  # Optionally specify domains to include
        "exclude_domains": []  # Optionally specify domains to exclude
    }

    response = requests.post(TAVILY_API_ENDPOINT, json=payload, headers=headers)

    if response.status_code == 200:
        results = response.json().get("results", [])
        return results
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Example usage
if __name__ == "__main__":
    query = "What is artificial intelligence?"
    results = search_tavily(query)
    for idx, result in enumerate(results):
        print(f"{idx + 1}. {result['title']}: {result.get('content', 'No content')}")
        if 'answer' in result:
            print(f"Answer: {result['answer']}")
        if 'image' in result:
            print(f"Image: {result['image']}")
        if 'raw_content' in result:
            print(f"Raw Content: {result['raw_content']}\n")
