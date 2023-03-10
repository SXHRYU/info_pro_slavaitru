FROM python:alpine3.16

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py",  runserver]
