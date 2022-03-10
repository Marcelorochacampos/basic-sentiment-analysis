FROM python:3.8-slim as app

WORKDIR /app

COPY . ./

RUN pip3 install -r requirements.txt

EXPOSE 7575

CMD ["python3", "main.py"]