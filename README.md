# Simple CRM system powered by Python 3 and FastAPI

### Starting:
1. Install dependences from `requirements.txt`
```shell
pip install -r requirements.txt
```
2. Do a migrations
```shell
alembic init alembic
```
Next you need set URI to database in `alembic.ini` and set metadata in `alembic/env.py`\
Next make migrations:
```shell
alembic revision --autogenerate
```
And do a migrations:
```shell
alembic upgrade head
```
3. Setting enviroment
Rename file `.env.simple` to `.env` and fill variables with values.
4. Start by uvicorn
```shell
uvicorn src.app:app --host 0.0.0.0 --port 8080
```

### Endpoints
1. POST `/api/users` - create user
2. PATCH `/api/users` - update current user
3. POST `/api/login` - get a message to email for confirm login
4. GET `/api/login` - get a session token
