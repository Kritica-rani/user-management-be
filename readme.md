# User Management Backend

A FastAPI-based backend service for managing users, featuring user creation, listing, and deletion operations with SQLAlchemy ORM and Docker containerization.

## Live Demo

The API is hosted at: [https://user-management-be-6oll.onrender.com](https://user-management-be-6oll.onrender.com)

## Features

- User management with create, list, and delete operations
- FastAPI framework for high-performance API development
- SQLAlchemy ORM for database interactions
- Docker containerization for easy deployment
- CORS middleware for frontend integration

## Tech Stack

- Python 3.10
- FastAPI
- SQLAlchemy
- Uvicorn ASGI server
- Docker
- Pydantic for data validation

## Running Locally

### Prerequisites

- Python 3.10+
- Docker and Docker Compose (optional)

### Option 1: Using Python Directly

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd user-management-be
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. The API will be available at: [http://localhost:8000](http://localhost:8000)

### Option 2: Using Docker

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd cd user-management-be
   ```

2. Build and run the Docker container:

   ```bash
   docker build -t user-management-backend .
   docker run -p 8000:8000 user-management-backend
   ```

3. The API will be available at: [http://localhost:8000](http://localhost:8000)

## API Documentation

Once the server is running, you can access the interactive API documentation:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

### Endpoints

#### Users

- **GET** `/users/` - List all users
- **POST** `/users/` - Create a new user
- **DELETE** `/users/{user_id}` - Delete a user by ID

## Deployment

The application is currently deployed on [Render](https://render.com) at [https://user-management-be-6oll.onrender.com](https://user-management-be-6oll.onrender.com).
