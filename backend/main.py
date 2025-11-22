import sys
import os
# add current directory to path so that it helps to import other modules in the project
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# __file__ is a special variable which has the pwd of the current working file

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.tasks import router as tasks_router
from database import engine, Base


# Base is created in database, and using Base, the table model(in models.py) is created
#Base.metadata has all the data about the table name, columns, primary key, data types and indexes etc
Base.metadata.create_all(bind=engine) #now this creates the table
# drop_all() to drop the table

# Base.metadata.tables.keys()) will print the table name

app = FastAPI(title="Task Tracker API")

# Add CORS middleware
app.add_middleware( 
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Task Tracker API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)