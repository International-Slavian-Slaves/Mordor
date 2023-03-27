FROM python:latest

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001 8001

CMD gunicorn --bind 0.0.0.0:8001 wsgi1:app | gunicorn --bind 0.0.0.0:8002 wsgi2:app