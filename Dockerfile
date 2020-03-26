FROM python:3.7-alpine
MAINTAINER Super App Ltda

ENV PYTHONBUFFERED 1 

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app  
#Creates an empty directory we are gonna store our source code
WORKDIR /app    
#Change to default directory
COPY ./app /app 
#Copies from our local machine ./app folder to the /app folder on our image

RUN adduser -D user
#user that runs processes from our project
USER user
#switch the user to the user we just created. This is done for security purposes, 
#if we dont do this the image will be run with our root account which is not recommended
