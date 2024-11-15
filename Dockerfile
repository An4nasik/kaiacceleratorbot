FROM ollama/ollama
WORKDIR /app
RUN apt update
RUN apt-get install -y python3
RUN apt install -y python3-pip
COPY requirements.txt ./
COPY main.py ./
COPY add.py ./
COPY handlers.py ./
COPY answer.py ./
COPY company_info.txt ./
COPY data ./data
COPY db ./db
COPY .env ./
RUN pip install -r requirements.txt



