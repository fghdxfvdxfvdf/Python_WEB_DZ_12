docker run --name hw_12-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -e POSTGRES_DB=hw_12 -d postgres


alembic init migrations
alembic revision --autogenerate -m 'Init'
alembic upgrade head

python -m uvicorn main:app --host localhost --port 8000 --reload



max     qwerty
lisa    1234
zik     147852      zik@example.com


http://localhost:8000/api/auth/signup

{
  "id": 3,
  "username": "zik",
  "email": "zik@example.com",
  "avatar": "https://www.gravatar.com/avatar/f1c1c08404b9ca35a80e1db198056763",
  "roles": "user"
}

http://localhost:8000/api/auth/login

Bearer