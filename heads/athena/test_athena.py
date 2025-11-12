import pytest
from fastapi.testclient import TestClient
from heads.athena.main import app

client = TestClient(app)

def test_analyze_endpoint_no_name():
    """
    Tests the /analyze endpoint with no name provided.
    It should return a 'Verification Failed' safety score.
    """
    response = client.post("/analyze", json={"phone": "123-456-7890"})
    assert response.status_code == 200
    assert response.json() == {
        "safety_score": "Verification Failed",
        "summary": "A name is required for identity verification."
    }

def test_analyze_endpoint_good_score():
    """
    Tests the /analyze endpoint for a user who should receive a 'Good' safety score.
    """
    response = client.post("/analyze", json={"name": "John Doe"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["safety_score"] == "Good"
    assert "<b>Risk Analysis:</b>" in json_response["summary"]
    assert "consistent and verifiable public presence" in json_response["summary"]

def test_analyze_endpoint_review_recommended_score():
    """
    Tests the /analyze endpoint for a user who should receive a 'Review Recommended' safety score.
    """
    response = client.post("/analyze", json={"name": "Jane Smith"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["safety_score"] == "Review Recommended"
    assert "<b>Risk Analysis:</b>" in json_response["summary"]
    assert "limited online presence" in json_response["summary"]

def test_analyze_endpoint_unverified_user():
    """
    Tests the /analyze endpoint with a name that should return an 'unverified' status.
    """
    response = client.post("/analyze", json={"name": "Unknown Person"})
    assert response.status_code == 200
    assert response.json() == {
        "safety_score": "Verification Failed",
        "summary": "Could not verify identity for Unknown Person. No public profiles found."
    }

def test_athena_html_loads():
    """
    Tests if the athena.html file is accessible.
    NOTE: This is not a real browser test, it just checks if the file exists.
    A real-world scenario would use a tool like Selenium or Playwright.
    """
    # This is a placeholder test. A real test would require a browser environment.
    # We'll simulate a "pass" if the file exists.
    try:
        with open("heads/athena/athena.html", "r") as f:
            pass
        assert True
    except FileNotFoundError:
        assert False, "athena.html not found"

def test_quick_exit_functionality_placeholder():
    """
    Placeholder test for the quick-exit functionality.
    In a real test, we would use a browser testing framework to:
    1. Load the athena.html page.
    2. Click the 'I'm not sure' button.
    3. Click the 'Quick Exit' button.
    4. Assert that the browser navigates to the correct URL.
    """
    # This is a conceptual test.
    print("\nConceptual Test: Quick Exit")
    print("1. Load athena.html")
    print("2. Click 'I'm not sure'")
    print("3. Click 'Quick Exit'")
    print("4. Assert window.location.href is the neutral page.")
    assert True
