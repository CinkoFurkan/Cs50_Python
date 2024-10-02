# Flight Finder

## Introduction

Flight Finder is a Python application that allows users to search for the cheapest flight options between two locations. The user inputs the IATA codes for the origin and destination, selects departure and return dates, and specifies the number of passengers. The app then retrieves the cheapest available flights using the Amadeus API and displays the total price in Euros.

This project was created as part of the **CS50x** course by **Harvard University**. The video demonstration of this project can be found on YouTube, along with my certificate of completion.

---

## Features

- **Flight Search:** Enter the origin, destination, departure, and return dates to find the cheapest flight.
- **Price Formatting:** Display the flight price in a user-friendly format (up to two decimal places).
- **Date Validation:** Ensure the input dates are valid and that the return date is later than the departure date.
- **Passenger Input Validation:** Allow only positive integers for the number of passengers.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/CinkoFurkan/flight-finder.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the Amadeus API access token as an environment variable:
   ```bash
   export AMADEUS_ACCESS_TOKEN="your_access_token"
   ```

---

## Usage

1. Run the program:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter:
   - Origin and destination IATA codes
   - Departure and return dates (YYYY-MM-DD format)
   - Number of passengers

The app will return the cheapest flight price if available.

---

## Running Tests

Unit tests are available for the helper functions. You can run the tests using `pytest`:

1. Install `pytest`:
   ```bash
   pip install pytest
   ```
2. Run the tests:
   ```bash
   pytest test.py
   ```

---

## YouTube Project Video

You can watch a video demonstration of the project on YouTube:

[Flight Finder Project Video](https://youtu.be/yGnPl_PquI8?si=cIhgxES5Dpy6IgiI)

---

## Certificate

I completed this project as part of the **CS50x** course offered by Harvard University. You can view my certificate here:

[CS50x Certificate - Furkan Çinko](https://certificates.cs50.io/b41f7fef-4c80-4b90-9524-76d7f1c0569b.pdf?size=letter)

---

## Acknowledgments

- This project was developed as part of the **CS50x** course by **Harvard University**.
- Special thanks to the **Amadeus API** for providing flight search services.

---

### Contact

For any inquiries, you can reach me at **furkan_cinko@outlook.com**.

