# IQDuel Assessment

Welcome to IQDuel Assessment! This repository contains my django backend assessment for IQDuel Company

## Project Overview

IQDuel is a web platform for managing online gaming leagues, tournaments, and player competitions, providing essential tools for competitive gaming organization and statistics tracking.

## Getting Started

### Prerequisites

- Python 3.10.12

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)  # Replace with your repo URL
    cd league_management  # Go to the project directory
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **(Optional) Create Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

## Running the Development Server

1.  **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Test (for WebSockets):**

    ```bash
    const socket = new WebSocket("ws://localhost:8000/ws/league/<league-id>/");
      socket.onmessage = function (event) {
      console.log("Received:", event.data);
      };
      socket.onopen = function () {
      socket.send(JSON.stringify({ message: "Connection opened" }));
      };
    ```

## API Endpoints

- **Leagues:**
  - `GET /api/leagues/`: List all leagues.
  - `POST /api/leagues/`: Create a new league.
  - `GET /api/leagues/{id}/`: Retrieve a specific league.
  - `PUT /api/leagues/{id}/`: Update a league.
  - `DELETE /api/leagues/{id}/`: Delete a league.
- **Players:**
  - `POST /api/players/`: Register a new player.
- **Matches:**
  - `GET /api/leagues/{league_id}/matches/`: List matches for a league.
- **Matchmaking:**
  - `POST /api/leagues/{league_id}/matchmaking/`: Perform matchmaking for a league.

## WebSocket Endpoint

- `ws://localhost:8000/ws/league/<league-id>/`: For live match updates

## Author

YOUR_NAME

## License

This project is licensed under the [LICENSE NAME] - see the [LICENSE.md](LICENSE.md) file for details.
