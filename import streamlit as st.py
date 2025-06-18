import streamlit as st
import pandas as pd
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# Load and preprocess data
def load_data():
    file_path = 'Book12 (1).xlsx'  # Replace with your file path if running locally
    data = pd.ExcelFile(file_path)
    sheet1_data = data.parse('Sheet1')
    
    # Select relevant columns
    relevant_columns = ["Date", "Time", "Totalizer (m3)", "Consuption"]
    refined_data = sheet1_data[relevant_columns]

    # Clean and preprocess
    refined_data["Date"] = pd.to_datetime(refined_data["Date"], errors="coerce")
    refined_data["Time"] = pd.to_timedelta(refined_data["Time"], errors="coerce")
    refined_data["Totalizer (m3)"] = pd.to_numeric(refined_data["Totalizer (m3)"], errors="coerce")
    refined_data["Consuption"] = pd.to_numeric(refined_data["Consuption"], errors="coerce")
    refined_data = refined_data.dropna(subset=["Date", "Time"])

    return refined_data

# Create insights function
def get_insights(data, query):
    # Here, you integrate the LlamaIndex (GPTSimpleVectorIndex) to process queries
    # Placeholder for now
    return "This is a placeholder response to your query: '{}'".format(query)

# Streamlit app
def main():
    st.title("Water Flow Data Insights Chatbot")

    # Load data
    data = load_data()
    st.subheader("Dataset Overview")
    st.dataframe(data.head())

    # User query
    st.subheader("Ask a question about the water flow data")
    query = st.text_input("Enter your question here:")

    if st.button("Get Insight"):
        if query:
            # Get insights from the query
            response = get_insights(data, query)
            st.subheader("Insight")
            st.write(response)
        else:
            st.warning("Please enter a question to proceed.")

if __name__ == "__main__":
    main()
