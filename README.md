# Bus Ticket Booking System

## Project Overview

The Bus Ticket Booking System is a web-based application that allows users to search for buses, view available seats, book tickets, and manage reservations online. This project simplifies the ticket booking process and provides a user-friendly interface for passengers and administrators.

## Features

### User Features

* User Registration and Login
* Search Buses by Source and Destination
* View Available Buses
* Select Seats
* Book Tickets
* View Booking History
* Cancel Bookings
* Download/Print Ticket

### Admin Features

* Admin Login
* Add New Buses
* Update Bus Details
* Delete Bus Information
* Manage Routes and Schedules
* View All Bookings
* Manage Users

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Backend

* Python
* Djangorestframework

### Database

* MySQL

## Project Structure

```text
BusTicketBooking/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── busbooking/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── templates/
├── static/
├── users/
├── bookings/
└── database/
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/uppellidayakar/BusTicketBooking.git
```

### 2. Navigate to Project Directory

```bash
cd BusTicketBooking
```

### 3. Create Virtual Environment

```bash
python -m venv env
```

### 4. Activate Virtual Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Database

Update database settings in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'BusTicketBooking',
        'USER': 'root',
        'PASSWORD': 'd@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Start Development Server

```bash
python manage.py runserver
```

### 9. Open Browser

```text
http://127.0.0.1:8000/
```

## Database Tables

* Bus
* Seat
* Booking
* Passenger
* Payment

## Future Enhancements

* Online Payment Gateway Integration
* Email Notifications
* SMS Notifications
* Seat Layout Visualization
* Mobile Application Support

## Learning Outcomes

* Django Framework
* MySQL Database Integration
* CRUD Operations
* Authentication and Authorization
* MVC/MVT Architecture
* Web Application Development

## Author

Uppelli Dayakar

## License

This project is developed for educational and learning purposes.

