FROM ollama/ollama
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
COPY main.py ./
COPY add.py ./
COPY handlers.py ./
COPY answer.py ./
COPY company_info.txt ./
COPY data ./data
COPY db ./db
COPY .env ./
RUN apt-get -y update; apt-get -y install curl
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama run llama3:8b
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
