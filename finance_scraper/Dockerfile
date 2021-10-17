FROM python:3.7

WORKDIR /opt/app

COPY . .

RUN pip install Flask

EXPOSE 5000

CMD ["python3", "-m", "main.py", "run", "--host=0.0.0.0"]
CMD ["python3", "-m", "rest_api", "run", "--host=127.0.0.1"]