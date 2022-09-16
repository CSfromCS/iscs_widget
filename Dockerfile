FROM python:3.9.14-slim-buster
ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
COPY . ./
CMD [ "python3","manage.py","runserver","8080"]
