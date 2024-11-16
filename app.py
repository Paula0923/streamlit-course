import streamlit as st
import pandas as pd

#################### PAGE SETUP ###############

# Set up the page
st.set_page_config(
    page_title="Superhero App",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

st.title("What's your Superhero Name? 😎") # emojis: press "windows key" und "." zusammen

#################### USER INPUTS ###############

# 1. User Input
fav_hus = st.text_input("Enter your favourite Lexie:", placeholder="The One")

# 2. User Input
fav_wife = st.text_input("Enter your favourite Polly:", placeholder="The Other One")

# 3. User Input
lucky_number = st.number_input("Enter the year you married:", min_value=1, step=1, value=2021)

# 4. Select box
superpower = st.selectbox("Select a superpower:", ["being married", "patience with my wifey", "kissing"])

# 5. Superhero Name
superhero_name = (f"{fav_color} and {fav_animal} since {lucky_number}")

# 6. Display superhero name and power
if st.button("Generate my Superhero Name") == True:
    st.write(f"Hello, {superhero_name}")
    st.write(f"Your superpower is {superpower}")