# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a simple RESTful web service using the FastAPI framework. Students will practice defining routes, handling JSON data, and structuring a Python web application for HTTP communication.

## 📝 Tasks

### 🛠️ Project Setup

#### Description
Initialize a new Python project, install FastAPI and an ASGI server (such as `uvicorn`), and create a basic application file.

#### Requirements
Completed program should:

- Create a virtual environment (recommended)
- Install `fastapi` and `uvicorn` via pip
- Define an `app` instance in a Python file (e.g. `main.py`)
- Be able to start the server with `uvicorn main:app --reload`


### 🛠️ Define Endpoints and Data Models

#### Description
Use Pydantic models to represent request and response payloads. Implement CRUD endpoints for a simple resource (for example, `items` or `users`).

#### Requirements
Completed program should:

- Define at least one Pydantic model for input/output data
- Implement `GET`, `POST`, `PUT`, and `DELETE` routes
- Use path and query parameters appropriately
- Return JSON responses with proper status codes


### 🛠️ Validation and Error Handling

#### Description
Add input validation and appropriate error responses. Ensure the API handles missing data and invalid requests gracefully.

#### Requirements
Completed program should:

- Validate incoming JSON against Pydantic models
- Return `400` errors for invalid payloads
- Handle cases where requested resources do not exist with `404` status


### 🛠️ Testing with HTTP Client

#### Description
Demonstrate the API using a command‑line tool such as `curl` or a GUI client like Postman. Provide example commands in the README.

#### Requirements
Completed program should:

- Include at least one example `curl` command in the README
- Show sample request and response bodies


---

Feel free to expand the service with additional features once the core requirements are met!