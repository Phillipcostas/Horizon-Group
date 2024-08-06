# Horizon - Virtual Travel Assistance App

Welcome to Horizon, your ultimate virtual travel assistant. Horizon is designed to help you manage your travel plans effortlessly, providing features to track itineraries, explore destinations, and receive timely notifications and updates. This README file will guide you through the setup and usage of the Horizon app.

### <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="50" height="50"> Git: 
  [Clint Eastman](https://github.com/ClintEastman01)   
  [Phillip Costas](https://github.com/PhillipCostas)   
  [Steven Macias](https://github.com/stvnmcs)   
  [Steven Zhang](https://github.com/zjplove3618739792)   
  [Joseph Cho](https://github.com/josephcho29)


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication:** Secure sign-up and login for users.
- **Itinerary Management:** Create, and update travel itineraries.
- **Virtual Suitcase & Packing Assistant:** Create, update and delete items to bring.
- **Interactive Itinerary:** Invite others and comment on each other's trip Itinerary.
- **Destination Explorer:** Discover new destinations with detailed information.
- **Interactive Map:** View your travel destinations on an interactive map.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Django 4.2+
- Virtualenv

### Steps

1. **Clone the Repository:**
```bash   
git clone https://github.com/yourusername/horizon.git
cd horizon
```
   
2. **Create and Activate a Virtual Environment:**
```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run Migrations:**
```bash
python manage.py migrate
```

5. **Create a Superuser:**
```bash
python manage.py createsuperuser
```

6. **Start the Development Server:**
```bash
python manage.py runserver
```

The app should now be running at http://127.0.0.1:8000/.

## Usage

### User Registration and Login

Navigate to http://127.0.0.1:8000/ and register for a new account.
Log in with your credentials to access the dashboard.

### Managing Itineraries
Use the "Add Itinerary" button to create a new travel plan.
Update or delete existing itineraries from your dashboard.

### Exploring Destinations
Visit the "Explore" section to discover new travel destinations.
Get detailed information about each destination, including points of interest and travel tips.

### Notifications
Receive notifications about upcoming trips, changes in itineraries, and personalized travel recommendations.

### Interactive Map
View your travel destinations on an interactive map for better visualization and planning.

### Contributing

We welcome contributions to Horizon! To contribute:

1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit them:
```bash
git commit -m 'Add some feature'
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name.
```
5. Open a pull request.

Please make sure to update tests as appropriate.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For questions, feedback, or support, please contact us at support@horizonapp.com.

Thank you for using Horizon! We hope it enhances your travel experiences.

Feel free to modify this README file to better suit the specific details and requirements of your project.
