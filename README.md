# League Management and Matchmaking System

This project implements a backend service for managing leagues and performing matchmaking between players in online games. It provides RESTful APIs for creating leagues, registering players, performing matchmaking, and retrieving match information. Optionally, it also includes WebSocket support for live match updates.

## Features

- **League Management:**
  - Create a league with a name and a maximum number of players.
  - Retrieve league details.
  - (Optional) Update/Delete Leagues.
- **Player Registration:**
  - Register a player in a specific league.
- **Matchmaking:**
  - Perform matchmaking between players in a league by randomly placing them into two-player groups. Handles odd numbers of players.
- **Match Retrieval:**
  - Retrieve a list of matches for a specific league.
- **(Optional) Live Match Updates:**
  - Use WebSockets to receive live match updates.

## Technologies Used

- Python
- Django
- Django REST Framework
- Channels (for WebSockets)
- PostgreSQL (recommended - or any database supported by Django)

## Installation

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
    pip install -r requirements.txt  # If you create a requirements file (recommended)
    # or
    pip install django djangorestframework channels daphne
    ```

4.  **Configure Database:**

    - Set up your PostgreSQL (or other) database.
    - Update the database settings in `league_management/league_management/settings.py`:

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',  # Or your database engine
              'NAME': 'your_database_name',
              'USER': 'your_database_user',
              'PASSWORD': 'your_database_password',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```

5.  **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **(Optional) Create Superuser:**

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

- `ws://your-server-address/ws/league/{league_id}/`: For live match updates.

## Testing

You can use tools like Postman or `curl` to test the API endpoints. The included example JavaScript code demonstrates how to connect to the WebSocket endpoint.

## Author

YOUR_NAME

## License

MIT (or your preferred license)
