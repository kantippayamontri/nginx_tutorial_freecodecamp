FROM python:3.11-slim

WORKDIR /root

COPY flask_app ./flask_app
COPY requirements.txt requirements.txt
COPY wsgi.py wsgi.py

RUN apt-get -y update
RUN pip install --upgrade pip
RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
# CMD ["exec","gunicorn", "-w","1" , "-b", "127.0.0.1", "flask_app:create_app(1)"]
# RUN  gunicorn -w 1 -b 127.0.0.1 "flask_app:create_app(1)"
CMD exec gunicorn -w 1 --bind 0.0.0.0:8000  "wsgi:app"

