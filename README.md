# Employee Management API

A REST API built with FastAPI for managing employee information.

This project is part of my Python backend development portfolio. It focuses on building a structured and maintainable API using PostgreSQL, SQLAlchemy, Pydantic, Alembic, and Git.

> **Project status:** In development. The main employee management features are implemented, but additional testing, documentation, and deployment work is still planned.

## Features

- Create employee records
- Retrieve all employees
- Retrieve an employee by ID
- Update employee information
- Delete employee records
- Validate request data with Pydantic
- Store employee information in PostgreSQL
- Access PostgreSQL using SQLAlchemy ORM
- Protect employee routes through user authentication
- Filter employees by name, department, and status
- Sort employees using validated fields and order values
- Paginate results using `skip` and `limit`
- Handle missing employees and invalid requests
- Handle database integrity errors
- Manage database changes with Alembic migrations
- Generate interactive API documentation automatically

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Alembic
- Uvicorn
- Git and GitHub
- OpenAPI / Swagger

## Requirements

Before running the project, make sure you have installed:

- Python 3.11 or later
- PostgreSQL
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/angelemmanuelesparzasantoyo/employee-management-api.git
cd employee-management-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Activate it on Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Configuration

Create a PostgreSQL database for the project.

Example database name:

```text
employee_management
```

Create a `.env` file in the project root and configure the database connection expected by the application.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/employee_management
```

Replace:

- `postgres` with your PostgreSQL username if it is different.
- `YOUR_PASSWORD` with your local PostgreSQL password.
- `employee_management` with your database name if it is different.

Do not upload your real `.env` file to GitHub.

Make sure `.env` is included in `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

You can include a safe `.env.example` file in the repository:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/employee_management
```

## Database Migrations

This project uses Alembic to manage database schema changes.

Apply all existing migrations:

```bash
alembic upgrade head
```

Create a new migration after modifying a SQLAlchemy model:

```bash
alembic revision --autogenerate -m "describe the change"
```

Apply the new migration:

```bash
alembic upgrade head
```

View the current migration:

```bash
alembic current
```

View the migration history:

```bash
alembic history
```

## Running the API

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Swagger UI can be used to review schemas, test endpoints, send requests, and inspect responses.

## Employee Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/employees/` | Retrieve employees |
| `GET` | `/employees/{employee_id}` | Retrieve an employee by ID |
| `POST` | `/employees/` | Create a new employee |
| `PUT` | `/employees/{employee_id}` | Update an employee |
| `DELETE` | `/employees/{employee_id}` | Delete an employee |

> Review Swagger UI to confirm whether the application adds an additional `/api` prefix to these routes.

## Filtering, Sorting, and Pagination

The employee list supports optional query parameters.

Example:

```http
GET /employees/?department=IT&status=Active&sort_by=name&order=asc&skip=0&limit=10
```

Supported operations include:

- Filter by employee name
- Filter by department
- Filter by status
- Sort by an allowed employee field
- Select ascending or descending order
- Skip a specific number of records
- Limit the number of returned records

### Pagination parameters

| Parameter | Description | Validation |
|---|---|---|
| `skip` | Number of records to skip | Must be `0` or greater |
| `limit` | Maximum number of records returned | Must be between `1` and `100` |

## Example Employee Request

```json
{
  "name": "Angel",
  "lastname": "Esparza",
  "email": "angel@example.com",
  "position": "Backend Developer",
  "department": "IT",
  "salary": 50000,
  "status": "Active",
  "hire_date": "2026-08-01",
  "phone": "4491234567"
}
```

The exact required fields, accepted values, and validation rules are available in Swagger UI at `/docs`.

## Validation

Employee information is validated using Pydantic schemas.

Current validation includes:

- Required employee information
- Minimum text lengths
- Valid email format
- Salary greater than zero
- Accepted employee status values
- Valid query parameters
- Pagination limits
- Valid sorting fields and order values

## Authentication

Employee routes use an authentication dependency to identify the current user before allowing access to protected operations.

Authentication-related behavior and schemas can be reviewed through Swagger UI.

## Error Handling

The API handles common errors such as:

- Employee not found
- Invalid employee information
- Invalid email format
- Invalid employee status
- Missing required information
- Invalid pagination values
- Invalid sorting parameters
- Database integrity conflicts

Errors are returned using appropriate HTTP status codes and readable messages.

## Project Architecture

The application separates responsibilities into different modules:

- **Routers:** Define API endpoints and request handling
- **Schemas:** Validate request and response data with Pydantic
- **Models:** Define PostgreSQL tables using SQLAlchemy
- **Database:** Configure database connections and sessions
- **Core:** Store authentication and security functionality
- **Migrations:** Track database changes using Alembic
- **Main application:** Configure FastAPI and register routers

This structure helps keep the project organized and maintainable.

## Development Workflow

This project uses Git and GitHub for version control.

The development workflow includes:

- Cloning repositories
- Creating feature branches
- Staging changes
- Creating descriptive commits
- Pushing and pulling changes
- Resolving merge conflicts
- Managing database migrations
- Developing features incrementally

## Roadmap

The following improvements are planned:

- Complete the remaining employee management features
- Improve authentication and authorization
- Add role-based permissions
- Add automated unit tests
- Add integration tests
- Add Docker support
- Add continuous integration with GitHub Actions
- Deploy the API publicly
- Add additional API examples
- Expand technical documentation

## Author

**Angel Emmanuel Esparza Santoyo**

- GitHub: https://github.com/angelemmanuelesparzasantoyo
- LinkedIn: https://www.linkedin.com/in/angel-esparza-11724a42v
- Email: angelesparzasanemm@gmail.com
