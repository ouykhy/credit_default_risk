import streamlit as st
import pickle
import numpy as np


# In[6]:


st.title("Credit default risk Demo")


# In[7]:


# Load the saved model
@st.cache_data
def load_model():
    with open("models/trained_model.pkl", "rb") as f:
        model = pickle.load(f)
        return model


# In[8]:


model = load_model()

st.title("Prédiction d'un risque de défaut de paiement")
st.write("Entrez vos données pour effectuer une prédiction :")

features = []
for i in range(model.n_features_in_):
    value = st.number_input(f"Feature {i+1}", step=0.1)
    features.append(value)

if st.button("Prediction"):
    X_sample = np.array(features).reshape(1, -1)
    prediction = model.predict(X_sample)[0]
    st.write(f"Risque de défaut de paiement: {prediction}")