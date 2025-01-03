from fastapi import FastAPI, Body
import joblib
import numpy as np


# In[14]:


app = FastAPI()

# Load the model when the application starts
model = joblib.load("models/trained_model.pkl")


# In[15]:


@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
@app.post("/predict")
def predict(data: list = Body(...)):
    arr = np.array(data)
    preds = model.predict(arr).tolist()
    return {"predictions": preds}
