import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="play_ground",
    page_icon="🎈",
    layout="centered"
)


# Load the dataset
# Ensure the dataset is in the same directory as this script, or provide the full path.
df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

st.title("Database_playground")
st.markdown("""
This web app allows users to explore and visualize data interactively. 
Utilize the sidebar to filter the dataset and customize the visualizations.
""")

data_filter = st.slider('What do you want?')
st.write("city:")

# Define a list of options for the multiselect dropdown
options = ['Option 1', 'Option 2', 'Option 3']

# Use st.multiselect to allow the user to select multiple options
selected_options = st.multiselect('Select your options:', options)

# Display the selected options
st.write('You selected:', selected_options)


 






