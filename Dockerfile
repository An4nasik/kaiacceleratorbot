FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt ./
COPY main.py ./
COPY add.py ./
COPY handlers.py ./
COPY answer.py ./
COPY company_info.txt ./
COPY .env ./
RUN pip install -r requirements.txt


CMD ["python", "main.py"]
