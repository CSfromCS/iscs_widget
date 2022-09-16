FROM python:3.9.14-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt
COPY . ./
CMD [ "python3","manage.py","runserver","8000"]
