from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200        # BLANK 1: the "OK" status code (3 digits)

def test_predict_setosa():
    response = client.post("/predict", json={
        "sepal_length": 5.1, "sepal_width": 3.5,
        "petal_length": 1.4, "petal_width": 0.2,
    })
    assert response.status_code == 200
    assert response.json()["species"] == "setosa"    # BLANK 2: which species for these numbers?

def test_predict_rejects_bad_input():
    response = client.post("/predict", json={"sepal_length": "hello"})
    assert response.status_code == 422        # BLANK 3: Pydantic validation error code
