Task 1

 requirements.txt (no psycopg2-binary if using SQLite)

 run.py starts Flask app

 CHANGES.md explains refactoring changes

 init_db.py initializes the database

 app/ folder with __init__.py, routes.py, models.py, services.py, database.py, validators.py

Task 2

 requirements.txt for Flask & pytest

 app/ folder with __init__.py, main.py, routes.py, services.py, database.py, utils.py

 tests/ folder with at least test_shortener.py

⚙ Running Instructions
 README.md at the root explains how to install, run, and test both tasks

 Each task can be run independently in its own folder with:

Create venv

Activate venv

Install requirements

Run app

🧪 Testing
Task 1

 All endpoints tested via Thunder Client/Postman:

GET /

POST /users

GET /users

GET /user/<id>

PUT /user/<id>

DELETE /user/<id>

GET /search?name=

POST /login

Task 2

 GET /health works

 POST /api/shorten returns short code

 GET /<short_code> redirects

 GET /api/stats/<short_code> returns stats

 pytest passes

Overview of both tasks

Setup instructions (venv, install, run) for Task 1 and Task 2

API endpoint list for each task

Testing instructions (e.g., Thunder Client, curl, pytest)