FROM python:3.8-alpine

WORKDIR /app
ENV FLASK_APP src/app.py
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

CMD ["flask", "run"]
