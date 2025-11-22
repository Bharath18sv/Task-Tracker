python3 -m venv venv
source venv/bin/activate
pip install uvicorn fastapi sqlalchemy
uvicorn main:app --reload --host 0.0.0.0 --port 9000
