from sqlmodel import SQLModel, create_engine, Session
from models import User, Group

sqlite_file_name = "fairshare.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:  # with will run session.close() when needed
        yield session


if __name__ == "__main__":
    create_db_and_tables()
    print("Database tables created successfully!")

