import streamlit
import requests

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

fruit_choice = streamlit.text_input("Select a fruit to get FruityVice Advice")

def get_fruityvice_advice(fruit_name):
      # Making an API call to get the data
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      # Using Pandas function to normalize the Json data, so the user can understand it easily
      FruityVice_Normalized = pandas.json_normalize(fruityvice_response.json())
      return FruityVice_Normalized


if not fruit_choice:
      streamlit.error("Please enter a fruit to get information")
else:
      fruitvice = get_fruityvice_advice(fruit_choice)
      streamlit.dataframe(fruitvice)


#Connecting to snowflake to extract data from snowflake table
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("Fruit Load contains : ")
streamlit.dataframe(my_data_row)

new_fruit = streamlit.text_input("What fruit would you like to add?")

if new_fruit: 
   my_cur.execute("Insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('"+new_fruit+"')")
   streamlit.write("Thanks for adding "+new_fruit)
else: 
   streamlit.write("")
#    my_cur.execute("Insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('"+new_fruit+"')")





