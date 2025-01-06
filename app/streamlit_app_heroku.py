import streamlit as st
import requests
import pickle
import numpy as np


# In[6]:


st.title("Credit default risk Demo via Heroku API")

@st.cache_data
def load_model():
    with open("models/logistic_regression_model.pkl", "rb") as f:
        model = pickle.load(f)
        return model


# In[8]:


model = load_model()

# In[8]:
features = []
for i in range(model.n_features_in_):
    value = st.number_input(f"Feature {i+1}", step=0.1)
    features.append(value)

api_url = "https://creditdefaultrisk-ed9d1d14ed09.herokuapp.com/"


if st.button("Predict"):
    try:
        feature_list = list(map(float, (feature for feature in features)))
        data = {"features": feature_list}

        # Try POST first
        response = requests.post(api_url, json=data, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            predictions = response.json().get("predictions", [])
            st.success(f"Predictions: {predictions}")
        elif response.status_code == 405 or response.status_code == 404:
            # Fallback to GET if POST fails
            response = requests.get(api_url, params={"features": features})
            if response.status_code == 200:
                predictions = response.json().get("predictions", [])
                st.success(f"Predictions: {predictions}")
            else:
                st.error(f"GET request failed with status {response.status_code}: {response.text}")
        else:
            st.error(f"POST request failed with status {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")