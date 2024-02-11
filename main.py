from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
import sys

sys.path.append(str(BASE_DIR))


from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from src.database.db import get_db
from src.routes import auth, contacts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", description="Main Page")
async def root():
    return {"title": "Contact App"}


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


app.include_router(auth.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")
