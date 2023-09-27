# README

## Description

This project is a simple API built using FastAPI in Python for handling transactions, including adding transactions, spending points, and checking the balance. The API stores transactions in memory and maintains a balance for each payer.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- Node.js installed (for running the test script)

## Project Structure

```
project_directory/
│
├── main.py  # The main file that contains the FastAPI app
└── tests.js  # The test script written in JavaScript for Node.js
```

## Setup and Installation

1. **Install FastAPI and Uvicorn:**

   FastAPI is the web framework used for building the API, and Uvicorn is an ASGI server that serves the FastAPI application.

   Open your terminal and run the following command:

   ```bash
   pip install fastapi uvicorn
   ```

2. **Install Node.js Packages:**

   You will need `node-fetch` for the test script to work.

   Run the following command:

   ```bash
   npm install node-fetch
   ```

## Running the API Server

1. Navigate to the project directory in the terminal.
2. Run the following command to start the Uvicorn server:

   ```bash
   uvicorn main:app --reload
   ```

   This command will start the server on `http://127.0.0.1:8000`.

## Testing the API

1. Ensure the API server is running.
2. Open a new terminal and navigate to the project directory.
3. Run the following command to execute the `tests.js` script:

   ```bash
   node tests.js
   ```

   This script will make requests to the API to add transactions, spend points, and get the balance, and it will output the responses.

## API Endpoints

1. **Add Transaction** (`POST /add`)

   - **Request Body:** JSON object with `payer` (string), `points` (integer), and `timestamp` (string in ISO 8601 format)
   - **Response:** Empty

2. **Spend Points** (`POST /spend`)

   - **Request Body:** JSON object with `points` (integer)
   - **Response:** Array of objects with `payer` (string) and `points` (integer)

3. **Get Balances** (`GET /balance`)

   - **Request Body:** None
   - **Response:** Object with payers as keys and balances as values

## Troubleshooting

- If you are unable to send requests to the API, ensure that the Uvicorn server is running and listening on `http://127.0.0.1:8000`.
- Ensure that all the necessary packages are installed.

## Contact Information

If you encounter any issues or have questions, feel free to contact the project author.
