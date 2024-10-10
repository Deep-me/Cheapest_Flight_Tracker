# Cheapest Flight Tracker ✈️

A Python-based application that tracks the cheapest flights using flight data APIs, object-oriented programming (OOP) principles, and Twilio for sending WhatsApp alerts when lower-priced flights are found. This project automatically monitors flight prices for specific destinations and notifies users of the best deals.

## Features
- **Flight Data Search**: Fetches flight information from an external API using the `FlightSearch` class.
- **Price Comparison**: Compares current flight prices with user-defined lowest prices.
- **WhatsApp Alerts**: Sends a WhatsApp message when a cheaper flight is found using Twilio.
- **Google Sheet Integration**: Uses Google Sheets to store and update destination data.

## Technologies Used
- **Python**: The programming language used for developing the application.
- **Twilio API**: For sending WhatsApp messages to alert users of cheap flights.
- **Amadeus API**: For fetching flight data and searching for flight deals.
- **Google Sheets API**: To store and manage destination data.
- **Object-Oriented Programming (OOP)**: Used to organize the codebase into classes for better modularity.

## Project Structure
- **main.py**: The main logic that ties all the modules together to track and notify about flight deals.
- **data_manager.py**: Handles data fetching and updating from the Google Sheets.
- **flight_search.py**: Responsible for interacting with the flight search API to retrieve flight data.
- **flight_data.py**: Structures the flight data received from the API.
- **notification_manager.py**: Manages sending notifications via WhatsApp using Twilio.

## Prerequisites
- **Python 3.x**: Ensure you have Python installed on your machine.
- **Twilio Account**: Sign up for a Twilio account to get your API key and a WhatsApp-enabled number.
- **Amadeus API Key**: Register with Amadeus to obtain an API key for accessing flight data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Deep=me/Cheapest-Flight-Tracker.git
   cd cheapest-flight-tracker
