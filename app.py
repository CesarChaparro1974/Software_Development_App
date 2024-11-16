"""
This Python module demonstrates filtering a DataFrame based on user selection 
and displaying the results in a Streamlit application.
"""
import pandas as pd
import streamlit as st
import plotly.express as px
import PIL
from PIL import Image

# Open the dataframe and filter it
df = pd.read_csv('vehicles_us.csv')
new_df = df[(df['model_year'] >= 1970) & (df['price'] >= 400)]

# Header of the app page
st.header('Vehicles market')
st.subheader('Here you can choose the car you want to buy')

# Image on the header
img = Image.open('car_sold.jpg')
WIDTH = 400
resized_image = img.resize((WIDTH, int(img.height * (WIDTH / img.width))),
                           resample=PIL.Image.Resampling.LANCZOS)
st.image(resized_image)

# Add slider for odometer range
st.caption(':New[Choose your parameters here]')
odometer_range = st.slider(
    "Slide to select and filter range of km of the car",
    value=(0, 990000)
)
actual_range = list(range(odometer_range[0], odometer_range[1] + 1))

# Add a checkbox for km filter
km_filter = st.checkbox('Cars with 12.000 km')
if km_filter:
    filtered_data = df[df.odometer.isin(actual_range)]
    filtered_data = filtered_data[df.odometer == 12000]
else:
    filtered_data = df[df.odometer.isin(actual_range)]

st.write('Here you have your options with car condition and price')

# Bar chart for price vs condition
fig = px.bar(filtered_data, x="condition", y="price", color_discrete_sequence=["#6CCB11"])
st.plotly_chart(fig)

# Add a sidebar for selecting transmission
transmission = df['transmission'].drop_duplicates()
choose = st.sidebar.selectbox('Select your vehicle:', transmission)

# Filter data based on transmission selection
new_df = df[df['transmission'] == choose]
new_df = df.dropna(subset=['model'])

# Ensure the 'price' column is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows where 'price' is NaN
new_df = df.dropna(subset=['price'])

# Filter price (excluding value 1 as per your code)
df_filtered = new_df[new_df['price'] != 1]

# Create results DataFrame with valid 'price' column
results_df = pd.DataFrame({'Model': df['model'], 'Price': new_df['price']})

# Display the results DataFrame in Streamlit
st.dataframe(results_df)

# List of cars from the selected transmission
st.write('List of cars from your transmission selection:')
st.dataframe(results_df)

# Divider
st.divider()

# Add a scatter plot for odometer distribution
st.write('Distribution by odometer')
fig2 = px.scatter(filtered_data, x='odometer', color_discrete_sequence=["#D4771D"])
st.plotly_chart(fig2)

# Divider
st.divider()

# Add a table with filtered recommended cars
st.write('Here are my recommended cars')
st.dataframe(filtered_data.sample(50))
