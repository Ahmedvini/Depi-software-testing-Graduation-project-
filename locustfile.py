import json
from locust import HttpUser, task, between

class BookerUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://restful-booker.herokuapp.com"
    token = None

    def on_start(self):
        """Get auth token when user starts"""
        credentials = {
            "username": "admin",
            "password": "password123"
        }
        response = self.client.post("/auth", json=credentials)
        if response.status_code == 200:
            self.token = response.json()["token"]
    
    @task(1)
    def get_booking_ids(self):
        """Get all booking IDs"""
        self.client.get("/booking")
    
    @task(2)
    def get_specific_booking(self):
        """Get details of a specific booking (using ID 1 as example)"""
        self.client.get("/booking/1")
    
    @task(1)
    def create_booking(self):
        """Create a new booking"""
        booking_data = {
            "firstname": "Test",
            "lastname": "User",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-02"
            },
            "additionalneeds": "Breakfast"
        }
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Cookie"] = f"token={self.token}"
        
        self.client.post(
            "/booking",
            json=booking_data,
            headers=headers
        )