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
fav_color = st.text_input("Enter your favourite color:", placeholder="Green")

# 2. User Input
fav_animal = st.text_input("Enter your favourite animal:", placeholder="Camel")

# 3. User Input
lucky_number = st.number_input("Enter your lucky number:", min_value=1, step=1, value=7)

# 4. Select box
superpower = st.selectbox("Select a superpower:", ["flying", "patience", "coding"])

# 5. Superhero Name
superhero_name = (f"{fav_color} {fav_animal} of {lucky_number}")

# 6. Display superhero name and power
if st.button("Generate my Superhero Name") == True:
    st.write(f"Hello, {superhero_name}")
    st.write(f"Your superpower is {superpower}")