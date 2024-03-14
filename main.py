import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="⚡", page_title='Sports Cars Dashboard')

st.title("SPORTS CARS ")
df = pd.read_csv("Sport_Car_Price.csv")
st.dataframe(df)

path = os.path.dirname(__file__)
path = os.path.join(path, "Sport_Car_Price.csv")

st.sidebar.header('Sports Cars')
data = st.sidebar.file_uploader("Upload Dataset", type=['csv', 'xlsx'])

menu = ['Cars Produced', 'Car Price', 'Analysis', 'About']
selection = st.sidebar.selectbox("Sports Cars Information ", menu)

st.sidebar.write('''The information here is about the prices of different sports cars 
from various manufacturers produced in different years. The information is useful for analyzing the prices of different
 sports cars and identifying trends in the market.''')

if selection == 'Cars Produced':

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Top 10 Car Makes ')
        grouped_data = df['Car Make'].value_counts(normalize=True)
        top_10_grouped_data = grouped_data.head(10)
        plt.figure(figsize=(8, 4))
        top_10_grouped_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Percentage of Produced Car Makes')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.ylabel('')  # Remove y-label
        st.pyplot(plt)

    with col2:
        st.subheader('Top 10 Car Models ')
        grouped_data = df['Car Model'].value_counts(normalize=True)
        top_10_grouped_data = grouped_data.head(10)
        plt.figure(figsize=(8, 4))
        top_10_grouped_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Percentage of Produced Car Models')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.ylabel('')  # Remove y-label
        st.pyplot(plt)

elif selection == "Car Price":
    st.subheader("Average price of each Car Make Top 19")
    df['Price (in USD)'] = df['Price (in USD)'].str.replace(',', '').astype(int)
    grouped_data = df.groupby('Car Make')['Price (in USD)'].mean().sort_values(ascending=False)

    top_19_grouped_data = grouped_data.head(19)
    plt.figure(figsize=(12, 8))  # Adjust figure size as needed
    top_19_grouped_data.plot(kind='bar', color='skyblue')
    plt.title('Average Price of Car Make')
    plt.xlabel('Car Make')
    plt.ylabel('Average Price in millions')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    st.pyplot(plt)

    bottom_19_grouped_data = grouped_data.tail(19)
    st.subheader("Average price of each Car Make Bottom 19")
    plt.figure(figsize=(12, 8))  # Adjust figure size as needed
    bottom_19_grouped_data.plot(kind='bar', color='purple')
    plt.title('Average Price of Car Make')
    plt.xlabel('Car Make')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    st.pyplot(plt)


elif selection == "Analysis":
    st.subheader('Data Summary')
    st.write(df.head(10))

    if st.checkbox("show shape"):
        st.write('Data Shape')
        st.write('{:,} rows; {:,} columns'.format(df.shape[0], df.shape[1]))

footer_temp = """
<!-- CSS  -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" 
type="text/css" rel="stylesheet" media="screen,projection"/>
<link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" 
integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
<footer class="page-footer grey darken-4">
<div class="container" id="aboutapp">
<div class="row">
<div class="col l6 s12">
<h5 class="white-text">Sports Cars App</h5>
<h6 class="grey-text text-lighten-4">This is my Sports Cars Project .</h6>
<p class="grey-text text-lighten-4">October 2024 Cohort</p>
</div>
<div class="col l3 s12">
<h5 class="white-text">Connect With Us</h5>
<ul>
<a href="https://www.facebook.com/SportsCars/" target="_blank" class="white-text">
<i class="fab fa-facebook fa-4x"></i>
</a>
<a href="https://www.linkedin.com/company/Sports_Cars" target="_blank" class="purple-text">
<i class="fab fa-linkedin fa-4x"></i>
</a>
<a href="https://www.youtube.com/SportsCars" target="_blank" class="red-text">
<i class="fab fa-youtube-square fa-4x"></i>
</a>
<a href="https://www.twitter.com/SportsCars" target="_blank" class="blue-text">
<i class="fab fa-twitter-square fa-4x"></i>
</a>
</ul>
</div>
</div>
</div>
"""

if selection == 'About':
    st.header("About App")
    components.html(footer_temp, height=500)
