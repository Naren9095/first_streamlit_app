import streamlit

streamlit.title("My Parents favourite Diner")

streamlit.header("Breakfast")
streamlit.text("🥣 Idly")
streamlit.text("🥗 Dosa")
streamlit.text("🥑🍞 Pongal")
streamlit.text("🐔 Boiled Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index("Fruit")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("FruityVice Advice! Check this once")

import requests
# Making an API call to get the data
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# Using Pandas function to normalize the Json data, so the user can understand it easily
FruityVice_Normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(FruityVice_Normalized)




