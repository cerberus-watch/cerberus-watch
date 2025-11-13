import pytest
from fastapi.testclient import TestClient
from heads.athena.main import app

client = TestClient(app)

def test_analyze_endpoint_no_name():
    response = client.post("/analyze", json={"name": ""})
    assert response.status_code == 200
    assert response.json()["safety_score"] == "Verification Failed"

def test_analyze_endpoint_good_score():
    response = client.post("/analyze", json={"name": "John Doe"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["safety_score"] == "Good"
    assert "consistent work history" in json_response["summary"]

def test_analyze_endpoint_review_recommended_score():
    response = client.post("/analyze", json={"name": "Jane Smith"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["safety_score"] == "Review Recommended"
    assert "limited activity" in json_response["summary"]

def test_analyze_endpoint_unverified_user():
    response = client.post("/analyze", json={"name": "Unknown Person"})
    assert response.status_code == 200
    assert response.json()["safety_score"] == "Verification Failed"
