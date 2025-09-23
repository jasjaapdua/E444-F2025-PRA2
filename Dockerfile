FROM python:3.12-slim

# environment variable setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=hello.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# set working directory inside docker container
WORKDIR /app

# copy and install requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of src code
COPY . /app/

# tells docker to listen on port 5000 (inside container)
EXPOSE 5000

# run the flask run command
CMD ["flask", "run"]
