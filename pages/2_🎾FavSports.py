import pymongo as pm
from pymongo import MongoClient
import streamlit as st 


client = MongoClient("localhost", 27017)

db = client['practicedb']

my_collection = db["Sports"]

st.title("Tell Us About your Favourite Sports")

Person_Name = st.text_input("Enter your name:")
Fav_sports = st.text_input("Enter your Fav Sports:")
Fav_player = st.text_input("Enter your Fav Player:")
About_sports = st.text_input("Tell us why do you like this sports:")

Do_You_Play = st.radio("DO You Know To Play:", ("YES", "NO"))


submit_button = st.button(label="Submit")

if submit_button:
    if Person_Name and Fav_sports:
        data ={
            "Name": Person_Name,
            "FavSport": Fav_sports,
            "FavPlayer": Fav_player,
            "KnowTOPlay": Do_You_Play,
            "AboutSports": About_sports,
            }
        result = my_collection.insert_one(data)

        st.success(f"All the fields are entered in the id:{result.inserted_id}")

    else:
        st.error("Fill all the fields")

