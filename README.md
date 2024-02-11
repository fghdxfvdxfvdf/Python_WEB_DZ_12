docker run --name hw_12-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -e POSTGRES_DB=hw_12 -d postgres


alembic init migrations
alembic revision --autogenerate -m 'Init'
alembic upgrade head

python -m uvicorn main:app --host localhost --port 8000 --reload

SECRET_KEY = "secret_key"
