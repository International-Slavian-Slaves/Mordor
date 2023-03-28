FROM python:latest

ENV FLASK_ENV=production
ENV WSGI1_KEY=YOUR_KEY1
ENV WSGI2_KEY=YOUR_KEY2

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001 8002

CMD gunicorn --bind 0.0.0.0:8001 wsgi1:app | gunicorn --bind 0.0.0.0:8002 wsgi2:app