import requests
import streamlit as st
st.title("My app")
st.subheader("Weather Hunter")
city = st.text_input("Entrez une ville: " )
api_key='8e4daf7cddd52c13aa9b45429d0ed1a0'
url = f" http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url).json()
button = st.button("Afficher la météo")
if button:
    st.write('Voici la température:', response['main']["temp"])
    st.write('Voici la humidité:', response['main']["humidity"])
    st.write('Voici la météo:', response['weather'][0]["description"])
    temp=response['main']["temp"]
    if temp<10:
        st.write(":(")
    elif temp<20:
        st.write(":/")
    else:
        st.write(":)")
