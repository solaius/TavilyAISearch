import streamlit as st
from search_summarization import summarize_search_results

# Set the title of the app
st.title("Tavily Langchain Demo")

# Create a dropdown for model selection
model_choice = st.selectbox(
    "Model:",
    ("OpenAI (Hosted)", "Mistral (vLLM)")
)

# Create input text area for user queries
user_input = st.text_area("Enter your query here:")

# Add a button to submit the query
if st.button("Submit"):
    # Process the query using summarize_search_results
    results, summary = summarize_search_results(user_input, model_choice)
    
    # Display the search results and summary
    st.write("Search Results:")
    for idx, result in enumerate(results):
        with st.expander(f"Result {idx + 1}: {result['title']}"):
            st.write(result.get('content', 'No content'))
            if 'answer' in result:
                st.write(f"**Answer:** {result['answer']}")
            if 'image' in result:
                st.write(f"**Image:** {result['image']}")
            if 'raw_content' in result:
                st.write(f"**Raw Content:** {result['raw_content']}\n")
    
    with st.expander("Summary"):
        st.write(summary)
