FROM python:3.9

WORKDIR /app

RUN apt-get update; apt-get upgrade -y; apt-get install -y sudo nano vim iputils-ping

COPY requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
