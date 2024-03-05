### Project Structure

```
alembic/
app/
    __pycache__/
    routers/
        __pycache__
        auth.py
        food.py
        order.py
        user.py
    init.py
    config.py
    database.py
    main.py
    models.py
    oauth2.py
    schemas.py
    utils.py

.gitignore
alembic.ini
env_sample.txt
requirements.txt
```

### Components



**alembic/:** Contains Alembic settings and migrations.


**routers/:** contains the application routers

**env_sample.txt:** Sample environment variable list. Create a `.env` file and provide values.

**config/:** Holds project settings.

**database.py:** Manages database connection, session settings, and the base database model.


**app/:** The main FastAPI project directory.
- **main.py:** Entry point of the application, with a router linking to the `user/` module.
  - **models.py:** Uses SQLAlchemy to draft the user table. Alembic handles migrations.
  - **schemas.py:** Defines schemas for create, details, login, and token requests.

### Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file and input environment variables.

3. Initialize database tables:
   ```
   alembic upgrade head
   ```

4. Start the application in development mode:
   ```
   uvicorn app.main:app --reload
   ```

5. Test the application by making requests to endpoints.


For detailed information, refer to the following resources:

- FastAPI documentation: https://fastapi.tiangolo.com/
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/

