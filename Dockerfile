FROM python:3.9

WORKDIR /

COPY app.py ./

CMD ["python3", "app.py"]