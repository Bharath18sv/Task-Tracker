from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
# sqlite3 is a builtin module in python
# sqlite has no server, no host and no port, it just stores data in a file in our local machine
SQLALCHEMY_DATABASE_URL = "sqlite:///./task_tracker.db" #this file is the database
# url syntax : <dialect+driver>://username:password@host:port/database_name
# here dialect means which database we are using, based on the dialect : sqlalchemy adapt's it's sql syntax
#here driver is SQLlite3 and dialect is SQLlite
# if we use mongodb, the dirver will be pymongo

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# check same thread = False ensures that the thread which was opened by other to connect to the same thread
# create_engine() is a factory function which returns the engine object (it'll not connect to database immediately)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit=False means the session will not immediately commit, it should be done manually eg: db.commit() and if something goes wrong we can rollback()
# bind=engine tells the session which database to connect

Base = declarative_base()

# re-usable dependency function to create a db session and close it after the endpoint returns a response
def get_db():
    db = SessionLocal() #session instance
    try:
        yield db #start the session where it left off
    finally:
        db.close()