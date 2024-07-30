import os
import httpx
from dotenv import load_dotenv
from tavily_search import search_tavily
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_community.llms import VLLMOpenAI
from langchain_core.runnables import RunnableSequence

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Access VLLM Information
VLLM_URL = str(os.getenv("VLLM_URL")) + "/v1"
VLLM_MODEL_NAME = os.getenv("VLLM_MODEL_NAME")


# Define your LangChain prompt template
template = """
Here are the top search results for "{query}":
{results}

Summarize the key points from these results.
"""

prompt = PromptTemplate(template=template, input_variables=["query", "results"])

def summarize_search_results(query, model_choice):
    results = search_tavily(query)
    formatted_results = "\n".join([f"{idx + 1}. {result['title']}: {result['content']}" for idx, result in enumerate(results)])
    inputs = {"query": query, "results": formatted_results}
    
    # Select the model based on the user's choice
    if model_choice == "OpenAI (Hosted)":
        llm = OpenAI(api_key=OPENAI_API_KEY)
    elif model_choice == "Mistral (vLLM)":
        llm = VLLMOpenAI(
                openai_api_key="EMPTY",
                openai_api_base=VLLM_URL,
                model_name=VLLM_MODEL_NAME,
                temperature=0,
                verbose=True,
                streaming=False,
                max_tokens=6000,
                async_client=httpx.AsyncClient(verify=False),
                http_client=httpx.Client(verify=False)
        )


    chain = RunnableSequence(prompt, llm)
    summary = chain.invoke(inputs)
    return results, summary

# Example usage
if __name__ == "__main__":
    query = "What is artificial intelligence?"
    model_choice = "OpenAI (Hosted)"
    results, summary = summarize_search_results(query, model_choice)
    print(summary)
