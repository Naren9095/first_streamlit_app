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

streamlit.multiselect("Pick your fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

