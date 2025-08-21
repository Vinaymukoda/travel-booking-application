# Travel Booking Application

A simple **Travel Booking Web Application** built with **Python (Django)** that allows users to:

* View available travel options (Flights, Trains, Buses)
* Book tickets
* Manage their bookings (view, cancel)

## Features

* User registration, login, and logout
* Profile management
* Travel options with filters for type, source, destination, and date
* Booking with seat availability validation
* Booking management (current & past bookings, cancelation)
* Responsive frontend using Bootstrap
* MySQL database support (SQLite for development)

## Requirements

  Python 3.10+
  Django 5+
  MySQL or SQLite
  Bootstrap (for UI)

## Setup Instructions

   pip install -r requirements.txt
   ```
3. Configure the database in `settings.py` (MySQL or SQLite)
4. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Run the development server:

   ```bash
   python manage.py runserver
   ```
6. Access the app at `http://127.0.0.1:8000`

## Deployment (AWS EC2 Example)

* Configure MySQL on AWS RDS
* Update allowed hosts and database settings
* Use Gunicorn + Nginx for production

## Bonus Features

* Search and filter travel options
* Unit tests for bookings and cancellations

## License

MIT License
