# CrewControl API

## Overview
The API provides a system to control users, teams, tasks, and departments.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Endpoints](#endpoints)
- [Tests](#tests)

## Quick Start

1. Install Docker and Docker Compose (if not already installed).
2. Navigate to the project directory where `docker-compose.yml` is located using CMD.
3. Create a `.env` file in the `app` directory with the following content:
    ```env
    DATABASE_URL='postgresql://crewcontrol:crewcontrol@crewcontrol_postgres:5432/crewcontrol_db'
    SECRET_KEY='41aa124df73c4eb6ce690120a1959640bc1e9ccab78dcd292355060778a89d4d'
    TEST_DATABASE_URL='postgresql://crewcontrol:crewcontrol@crewcontrol_postgres:5432/test_crewcontrol_db'
    ```
4. Start the application:
    ```sh
    docker compose up
    ```

## Endpoints

### Users

- **GET /users**: Retrieve a list of users
- **POST /users**: Create a new user
- **GET /users/{id}**: Retrieve a specific user by ID
- **PUT /users/{id}**: Update a specific user by ID
- **DELETE /users/{id}**: Delete a specific user by ID

### Teams

- **GET /teams**: Retrieve a list of teams
- **POST /teams**: Create a new team
- **GET /teams/{id}**: Retrieve a specific team by ID
- **PUT /teams/{id}**: Update a specific team by ID
- **DELETE /teams/{id}**: Delete a specific team by ID

### Tasks

- **GET /tasks**: Retrieve a list of tasks
- **POST /tasks**: Create a new task
- **GET /tasks/{id}**: Retrieve a specific task by ID
- **PUT /tasks/{id}**: Update a specific task by ID
- **DELETE /tasks/{id}**: Delete a specific task by ID

### Departments

- **GET /departments**: Retrieve a list of departments
- **POST /departments**: Create a new department
- **GET /departments/{id}**: Retrieve a specific department by ID
- **PUT /departments/{id}**: Update a specific department by ID
- **DELETE /departments/{id}**: Delete a specific department by ID

## Tests

To run the tests, use the `pytest` command in the Docker container.