# Python base image 
FROM python:3.10-slim

# Working directory 
WORKDIR /app

# install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# FastAPI server run 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]