
# Loan Creation API

## Project Description

Python application to integrate with the
Loan Creation REST API using HTTP POST requests.

## Technologies Used

- Python
- uv
- Requests
- python-dotenv
- REST API
- JSON

## Project Setup

### 1. Clone the repository

git clone <repository-url>

### 2. Navigate into the project

cd loan-creation-api

### 3. Install dependencies

uv sync

### 4. Configure environment variables

Create a .env file using .env.example.

Add the staging API configuration and credentials
provided by the authorized team.

### 5. Configure the request payload

Create loan_payload.json with an approved test payload.

### 6. Run the application

uv run python main.py

## API Details

Method: POST

Endpoint:
/gateway/v1/pos2/loan/publish

Query Parameter:
offerCodeId

Headers:
- UserId
- Type
- Content-Type
- Authorization

## Security

- Never commit .env.
- Never commit applicant personal information.
- Never expose API credentials.
- Use authorized staging test data.

## Dependencies

Dependencies are managed using uv and pyproject.toml.
