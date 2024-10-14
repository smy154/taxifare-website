import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''
# Input fields for user to enter the details of the ride
pickup_date = st.date_input("Enter the pickup date (YYYY-MM-DD)", value=datetime.date.today())
pickup_time = st.time_input("Enter the pickup time (HH:MM:SS)", value=datetime.time(12, 0))

# Combining date and time into a single datetime string
pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input("Enter pickup longitude", value=-73.950655)
pickup_latitude = st.number_input("Enter pickup latitude", value=40.783282)
dropoff_longitude = st.number_input("Enter dropoff longitude", value=-73.984365)
dropoff_latitude = st.number_input("Enter dropoff latitude", value=40.769802)
passenger_count = st.number_input("Enter passenger count", min_value=1, max_value=10, value=1)

''''''

url = 'https://wagon-data-tpl-image-1072314491692.europe-west1.run.app/predict'

if url == 'https://wagon-data-tpl-image-1072314491692.europe-west1.run.app/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button('Predict Fare'):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Predicted fare: ${prediction['fare']:.2f}")
    else:
        st.write("Error in API call. Please check the input values and try again.")
