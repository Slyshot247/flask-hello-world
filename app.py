from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Set the API endpoint for booking a ride
url = "https://api.rideshare.com/book"

@app.route('/book_ride', methods=['POST'])
def book_ride():
    # Get the user's pickup and dropoff locations from the request
    pickup_location = request.json['pickup_location']
    dropoff_location = request.json['dropoff_location']

    # Get the user's personal information from the request
    name = request.json['name']
    phone_number = request.json['phone_number']

    # Create a dictionary to store the user's information
    payload = {
        "pickup_location": pickup_location,
        "dropoff_location": dropoff_location,
        "name": name,
        "phone_number": phone_number
    }

    # Send a POST request to the API endpoint to book the ride
    response = requests.post(url, json=payload)

    # Check if the API returned a successful status code
    if response.status_code == 200:
        return jsonify({"status": "success", "message": "Ride booked successfully"})
    else:
        return jsonify({"status": "error", "message": "Failed to book ride"})

if __name__ == '__main__':
    app.run(debug=True)
