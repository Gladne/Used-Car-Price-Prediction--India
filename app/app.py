import streamlit as st
import pandas as pd
import numpy as np
import joblib

# load models, columns and encoders
model = joblib.load('/home/bellona/Documents/40 days Plan/ADS Capstone Project/models/car_price_model.pkl')
model_mean = joblib.load('/home/bellona/Documents/40 days Plan/ADS Capstone Project/models/model_mean.pkl')
global_mean = joblib.load('/home/bellona/Documents/40 days Plan/ADS Capstone Project/models/global_mean.pkl')
columns = joblib.load('/home/bellona/Documents/40 days Plan/ADS Capstone Project/models/car_columns.pkl')

st.set_page_config(page_title='Used Car Price Predictor', layout='centered')
st.title('Used Car Price Prediction')
st.write('Fill in the details below to predict the estimated Used Car Price')

vehicle_age = st.slider('Vehicle Age', 0, 30, 5)
km_driven = st.number_input('Kilometers Driven', 0, 500000)
model_name = st.text_input('Car Model')
brand_name = st.text_input('Car Brand')
max_power = st.slider('Maximum Engine Power', 10, 130, 60)
car_seats = st.number_input('Car Seats', 4, 7)

if st.button('Predict Price'):
    model_encoded = model_mean.get(model_name, global_mean)
    input_df = {
        'vehicle_age': vehicle_age,
        'km_driven': km_driven,
        'model': model_name,
        'brand': brand_name,
        'max_power': max_power,
        'seats': car_seats,
        'model_encoded': model_encoded
    }

    df = pd.DataFrame([input_df])

    df = df.reindex(columns=columns, fill_value=0)

    prediction_log = model.predict(df)[0]

    price = np.expm1(prediction_log)

    st.success(f'Estimated Price: ₹ {price:,.0f}')