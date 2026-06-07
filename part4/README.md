# HBnB Project - Part 4: Simple Web Client

This is the front-end web client for the HBnB application, built using HTML5, CSS3, and JavaScript ES6. It connects dynamically with the Flask REST API from Part 3.

## Features
* **User Login**: Authenticates users and stores JWT tokens securely in browser cookies.
* **Dynamic Places List**: Fetches and displays all available places from the API.
* **Client-Side Filtering**: Filters places by maximum price without reloading the page.
* **Place Details**: Shows extended information for each place, including description, price, and user reviews.
* **Review Submission**: Allows logged-in users to post ratings and comments for a place.

## File Structure
* `index.html` - The main dashboard displaying the list of places and price filter.
* `login.html` - The user authentication form.
* `place.html` - Detailed view for a specific place and its reviews.
* `add_review.html` - Form to submit a new review (Authenticated users only).
* `styles.css` - Custom UI styling and responsive layouts.
* `scripts.js` - JavaScript file handling API requests (Fetch), DOM updates, and session cookies.

## How to Run
1. Make sure your Part 3 Flask backend API is running on `http://127.0.0.1:5000`.
2. Open `index.html` directly in any modern web browser.
3. Login using the default admin credentials (`admin@hbnb.com` / `admin123`) to test all authenticated features.