"""
This Python module demonstrates filtering a DataFrame based on user selection 
and displaying the results in a Streamlit application.
"""
#import libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import PIL
from PIL import Image

#open the dataframe and filter the dataframe
df = pd.read_csv('vehicles_us.csv')
new_df = df[(df['model_year'] >= 1970) & (df['price'] >= 400)]

#header of the app page
st.header('Vehicles market')
st.subheader('Here you can choose the car you want to buy')

#image on the header
img = Image.open('car_sold.jpg')
WIDTH = 400
resized_image = img.resize((WIDTH, int(img.height * (WIDTH / img.width))),
                           resample=PIL.Image.Resampling.LANCZOS)
st.image(resized_image)

#add slider
st.caption(':New[Choose your parameters here]')

odometer_range = st.slider(
    "Slide to select and filter range of km of the car",
    value = (0, 990000))
actual_range = list(range(odometer_range[0], odometer_range[1]+1))

#add a checkbox
km_filter = st.checkbox('Cars with 12.000 km')

if km_filter:
    filtered_data = new_df[new_df.odometer.isin(actual_range)]
    filtered_data = filtered_data[new_df.odometer == 12000]
else:
    filtered_data = new_df[new_df.odometer.isin(actual_range)]

st.write('Here you have your options with car condition and price')

#add bar chart
fig = px.bar(filtered_data, x="condition", y="price", color_discrete_sequence=["#6CCB11"])
st.plotly_chart(fig)

# Add a sidebar
transmission = new_df['transmission'].drop_duplicates()
choose = st.sidebar.selectbox('Select your vehicle:', transmission)

# Filter data based on user selection
new_df = new_df[new_df['transmission'] == choose]
new_df = new_df.dropna(subset=['model'])

# Filter price within the filtered DataFrame
df_filtered = new_df[new_df['price'] != 1]

# Create results DataFrame
results_df = pd.DataFrame({'Model': new_df['model'], 'Price': new_df['price']})

st.write('List of cars from your transmission selection:')
st.dataframe(results_df)

#add a divider
st.divider()

#add a histogram
st.write('Distribution by odometer')
fig2 = px.scatter(filtered_data, x='odometer', color_discrete_sequence=["#D4771D"])
st.plotly_chart(fig2)

#add a divider
st.divider()

#add a table with filtered recommended cars
st.write('Here are my recommended cars')
st.dataframe(filtered_data.sample(50))
