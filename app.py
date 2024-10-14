import streamlit as st
import requests

'''
# TaxiFareModel front

- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_datetime = st.text_input("Enter the pickup datetime (YYYY-MM-DD HH:MM:SS)")
pickup_longitude = st.text_input("Enter the pickup longitude")
pickup_latitude = st.text_input("Enter the pickup latitude")
dropoff_longitude = st.text_input("Enter the dropoff longitude")
dropoff_latitude = st.text_input("Enter the dropoff latitude")
passenger_count = st.text_input("Enter the passenger count")

if st.button('Predict Fare'):
    url = 'https://wagon-data-tpl-image-1072314491692.europe-west1.run.app/predict'

    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": float(pickup_longitude),
        "pickup_latitude": float(pickup_latitude),
        "dropoff_longitude": float(dropoff_longitude),
        "dropoff_latitude": float(dropoff_latitude),
        "passenger_count": int(passenger_count)
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Predicted fare: {prediction['fare']}")
    else:
        st.write("Error in prediction request.")
