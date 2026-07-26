# 1. Start from a base image that already has Python
FROM python:3.11-slim

# 2. Set the working folder inside the container
WORKDIR /app

# 3. Copy requirements first, then install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of our app (main.py, model.joblib)
COPY . .

# 5. Document the port the app uses
EXPOSE 8000

# 6. Command that runs when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#                      │                  │
#          BLANK 1: the FastAPI object    BLANK 2: the address (NOT 127.0.0.1 — see below)
