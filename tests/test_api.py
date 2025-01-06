import numpy as np
from fastapi.testclient import TestClient
from app.main import app


# In[27]:


client = TestClient(app)


# In[30]:


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert "API is running" in res.json()["message"]

def test_predict():
    test_data = np.random.rand(1, 43).tolist()

    res = client.post("/predict", json=test_data)

    assert res.status_code == 200
    assert "predictions" in res.json()
    # assert isinstance(res.json()["probabilities"], list)
    # assert len(res.json()["probabilities"]) == 1