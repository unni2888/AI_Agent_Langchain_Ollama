FROM python:3.13-slim

WORKDIR /AI Agent

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .



CMD ["streamlit", "run", "main.py"]