1️ Major Issues Identified in Original Code
Poor Project Structure – All routes, DB logic, and validations mixed together in one file.

No Input Validation – Endpoints accepted any data without verifying required fields or formats.

Security Vulnerabilities – Passwords stored in plain text.

Hardcoded Configuration – Database URI and other settings hardcoded inside code.

Improper HTTP Status Codes – Used incorrect codes (e.g., returning 200 for errors).

No Error Handling – No try/except blocks for DB or request parsing errors.

No Tests – No automated test coverage for API behavior.



2️⃣ Changes Made
Reorganized Project Structure

Added app/ package containing:

__init__.py – Flask app creation and blueprint registration

routes.py – All API routes

services.py – Business logic separated from route handlers

database.py – Database initialization and SQLAlchemy setup

validators.py – Marshmallow schemas for request validation

models.py – SQLAlchemy models for User table

Added Validation

Used Marshmallow to validate inputs for user creation and update

Implemented Password Hashing

Used werkzeug.security to hash passwords and verify on login

Improved Config Management

Moved DB URI to a config variable (SQLite by default for local testing)

Correct HTTP Status Codes

201 Created for POST success

400 Bad Request for invalid input

404 Not Found for missing resources

Added Error Handling

Checks for invalid IDs and missing records

Added Basic Tests

Added pytest tests for health check and create user

3️⃣ Assumptions
SQLite is sufficient for local development — PostgreSQL can be added easily by updating DB URI

API authentication (JWT/session) is outside the scope of this refactor

4️⃣ Trade-offs
Chose SQLite over PostgreSQL for portability (avoids psycopg2 build issues)

Did not implement pagination or advanced filtering to keep focus on refactor
5️⃣ Future Improvements
Add JWT-based authentication and role management

Add pagination and sorting to /users endpoint

Implement rate limiting to prevent abuse

Expand automated test coverage

Add CI/CD pipeline for automated deployment