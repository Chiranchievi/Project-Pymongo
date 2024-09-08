import pymongo as pm
from pymongo import MongoClient
import streamlit as st 


client = MongoClient("localhost", 27017)

db = client['practicedb']

my_collection = db["Sports"]

#Text boxes for user input
User_name = st.text_input("Enter your name:")
Fav_sports = st.text_input("Enter your Favourite Sport:")


view_button = st.button("View")

if view_button:
    if User_name and Fav_sports:
        x = my_collection.find_one({"Name":f"{User_name}"})
    # x = x.items()
    st.text(f"Name: {x['Name']}") 
    st.text(f"Favourite Sports: {x['FavSport']}") 
    st.text(f"Favourite Player: {x['FavPlayer']}") 
    st.text(f"Whether do you play this game: {x['KnowTOPlay']}")
    st.text(f"why you like this sports:{x['AboutSports']}") 