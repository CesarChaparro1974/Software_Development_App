import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Car sales advertisements')
st.subheader('Here you can choose the car you want to buy')
import urllib.request
from PIL import Image
urllib.request.urlretrieve('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3HpHmTQ1nb9VPaYfsHatjvniLGN0Q6qL7bg&usqp=CAU'"gfg.png")
img = Image.open("gfg.png")
st.image(img)
st.caption(':New[Choose your parameters here]')

price_range = st.slider(
    "What is your budget range?",
    value = (200, 375000))



