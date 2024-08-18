# FootballFieldBooking

Football Field Booking Platform: A system for managing the reservation of football fields. Allows administrators to
manage field information, enables owners to edit and view their bookings, and provides users with the ability to search,
filter, and book available fields based on their location and availability.

## Getting Started

These instructions will help you run a copy of the project on your local machine for development and testing.

### Prerequisites

Install the following tools:

- Docker
- Docker Compose

### Installation and Launch

1. **Cloning the repository**:
    ```
    git clone https://github.com/ulugbekaxtamov/FootballFieldBooking.git
    ```

2. **Navigate to the project directory**:
    ```
    cd FootballFieldBooking
    ```

3. **Create `.env` files using examples**:
    ```
    cat example.env > .env
    ```

4. **Run Docker Compose**:
    ```
    docker-compose up --build
    ```

### API Documentation

Access the Swagger documentation for API details at:

```
http://127.0.0.1:8000/redoc/
```

```
http://127.0.0.1:8000/swagger/
```

# Project Structure

This document outlines the structure of the Django project.

## Directory Structure

```

├── README.md # This file
├── docker-compose.yaml # Docker Compose configuration for development
├── Dockerfile # Dockerfile for the main server
├── requirements.txt # Python dependencies
├── .env # Environment variables
├── config # Main Django project folder
│ ├── settings.py # Import Base class here
│ └── ...
├── api/ # Django project api (deprecated)
│ ├── v1/ # api version control
├── apps/ # Django project apps
│ ├── user/ # User management app
│ ├── base/ # Manage soft deletion and default fields
│ │ ├── apps.py
│ │ ├── models.py # Base class imported here
│ │ └── ...
│ ├── booking/ # Manage bookings
│ ├── football_field/ # Manage football fields

......
```

## Notes

- The `api/` directory is deprecated and should be replaced by the `apps/` directory.
- The `apps/` directory contains the core Django apps for user management, booking, and football field management.
- The `base/` app handles soft deletion and default fields for other apps.

Feel free to update this structure as your project evolves.
