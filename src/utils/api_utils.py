import requests
import random
import streamlit as st

def fetch_answer(query, retrieval_type, temperature):
    api_url = "https://app-bachelor-1.azurewebsites.net/api/query"

    headers = {
        "X-Retrieval-Type": str(retrieval_type),
        "X-Temperature": str(temperature),
        "X-OpenAI-Key": st.secrets["openai_key"],
        "X-Weaviate-Key": st.secrets["weaviate_key"]
    }

    if retrieval_type == 1:
        headers['X-Neo4j-Uri'] = st.secrets["neo4j_graph_uri"]
        headers['X-Neo4j-Password'] = st.secrets["neo4j_graph_password"]
    else:
        headers['X-Neo4j-Uri'] = st.secrets["neo4j_hybrid_uri"]
        headers['X-Neo4j-Password'] = st.secrets["neo4j_hybrid_password"]

    body = {
        "question": query
    }

    response = requests.post(api_url, headers=headers, json=body)

    try:
        response = requests.post(api_url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error occured: {e}")
    return None

def get_control_variables():
    retrieval_type = random.choice([0, 2])
    temperature = random.uniform(0.1, 0.9)

    return retrieval_type, temperature
