# Tavily AI Search

This project is a demonstration of a search and summarization application using LangChain and OpenAI.

## Features

- **Search**: Uses Tavily API to search for information.
- **Summarization**: Uses OpenAI's API to summarize search results.

## Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- OpenAI API Key
- Tavily API Key

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/solaius/TavilyAISearch.git
   cd TavilyAISearch
2. Virt Environment:
   ```sh
   python -m venv env
   env/scripts/acvitate
3. Install dependencies:
   ```sh
   python.exe -m pip install --upgrade pip
   pip install -r requirements.txt
4. Add Environment Varaiable in .env file
   ```sh
   Add TAVILY_API_KEY - https://app.tavily.com/home
   Add OPENAI_API_KEY - https://platform.openai.com/api-keys
4. Run app:
   ```sh
   streamlit run app.py