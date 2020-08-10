FROM python:3.8-alpine

WORKDIR /app
ENV FLASK_APP src/app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["flask", "run"]
