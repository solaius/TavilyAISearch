import os
from dotenv import load_dotenv
from tavily_search import search_tavily
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnableSequence

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define your LangChain prompt template
template = """
Here are the top search results for "{query}":
{results}

Create detailed summaries of the key points from these results.
"""

prompt = PromptTemplate(template=template, input_variables=["query", "results"])

# Create your LangChain model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Define the LangChain chain
def summarize_search_results(query):
    results = search_tavily(query, top_k=5)  # Ensure to pull more detailed results

    formatted_results = "\n".join([f"{idx + 1}. {result['title']}: {result.get('content', 'No content')}" for idx, result in enumerate(results)])
    inputs = {"query": query, "results": formatted_results}
    chain = RunnableSequence(prompt, llm)
    summary = chain.invoke(inputs)
    return results, summary

# Example usage
if __name__ == "__main__":
    query = "What is artificial intelligence?"
    results, summary = summarize_search_results(query)
    print("Search Results:")
    for idx, result in enumerate(results):
        print(f"{idx + 1}. {result['title']}: {result.get('content', 'No content')}")
        if 'answer' in result:
            print(f"Answer: {result['answer']}")
        if 'image' in result:
            print(f"Image: {result['image']}")
        if 'raw_content' in result:
            print(f"Raw Content: {result['raw_content']}\n")
    print("Summary:")
    print(summary)
