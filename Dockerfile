FROM python:3.10.1-slim-buster

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY main.py .

#Publish port
EXPOSE 5000

# command to run on container start
ENTRYPOINT [ "python", "./main.py" ]