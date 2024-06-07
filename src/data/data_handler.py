import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

@st.cache_resource
def init_client():
    return MongoClient(st.secrets["mongo_uri"], tlsCAFile=certifi.where())

client = init_client()
database = client.get_database("bachelor_db")

@st.cache_data()
def get_passages():
    collection = database.get_collection("passage")

    passages = collection.aggregate([{ '$sample': {'size': 10}}])
    
    return list(passages)

def save_to_db(query, result, correct):
    result["query"] = query
    result["correct"] = correct

    database.get_collection("result").insert_one(result)