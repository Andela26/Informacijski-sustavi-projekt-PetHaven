FROM python:3.13
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
