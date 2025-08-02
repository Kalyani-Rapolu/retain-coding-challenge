CHANGES.md – Task 1: User API Refactoring
1️⃣ Major Issues Identified in Original Code
Poor Project Structure – All logic in one file; no separation between routes, models, and database.

No Input Validation – API accepted any data without checking required fields or formats.

Security Vulnerabilities – Passwords stored in plain text; no hashing.

Hard-coded Configuration – Database URI and sensitive info were hard-coded.

Improper HTTP Status Codes – Success and error responses often returned wrong codes.

No Error Handling – Missing try/except blocks or graceful handling of database errors.

No Tests – No automated tests to verify core functionality.

2️⃣ Changes Made
Reorganized into Package Structure

app/ package with __init__.py, routes.py, models.py, services.py, database.py, and validators.py for clear separation of concerns.

Added Marshmallow Validation

Created UserSchema to validate input data for POST and PUT requests.

Implemented Password Hashing

Using werkzeug.security.generate_password_hash and check_password_hash.

Improved Config Management

Removed hard-coded DB URI; now using SQLite for demo purposes (easily switchable to PostgreSQL).

HTTP Status Codes Fixed

Used 201 Created for POST, 404 Not Found for missing resources, etc.

Error Handling Added

Checked for missing users and invalid credentials.

Basic Tests Added

pytest tests for health check and user creation.

3️⃣ Assumptions
SQLite database is sufficient for local demo; PostgreSQL can be enabled by changing the URI.

Password reset, JWT authentication, and role-based access are out of scope for this refactor.

4️⃣ Trade-offs
Chose SQLite over PostgreSQL for portability — avoids psycopg2 build issues and works out of the box.

Did not implement full authentication (JWT/session) to keep the focus on refactoring.

5️⃣ What I Would Do With More Time
Add JWT authentication and refresh tokens.

Add pagination, filtering, and sorting to /users endpoint.

Add rate limiting to prevent abuse.

Write more comprehensive test coverage.

Use environment-based configuration for dev/prod.
Must explain:

Issues in original code

Changes made

Assumptions/trade-offs

What I’d do with more time

