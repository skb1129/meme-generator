FROM python:stretch

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
