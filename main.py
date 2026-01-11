from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import User, Group

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Welcome to FairShare API!", "Status": "active"}


@app.post("/users/")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)  # adding user to session (no ID yet)
    session.commit()  # sending sql query to SQLite to add user, DB  assigns ID
    session.refresh(user)  # sending current data from DB to python. SELECT query
    return user


@app.post("/groups/")
def create_group(group: Group, session: Session = Depends(get_session)):
    session.add(group)
    session.commit()
    session.refresh(group)
    return group

@app.get("/groups/")
def read_groups(session: Session = Depends(get_session)):
    statement = select(Group)
    results = session.exec(statement)
    groups = results.all()
    return groups



