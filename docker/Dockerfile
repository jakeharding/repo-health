 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 ENTRYPOINT ["repo-health"]
 LABEL Description="This image supplies the server needed for repo-health."
 
 # Setting up database
 RUN apt-get update && apt-get install -y curl
 RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
 RUN apt-get install -y nodejs
 RUN mkdir /www

 WORKDIR /www
 COPY requirements.txt /www/
 RUN pip install -r requirements.txt
 COPY /repo_health/. /www/repo_health
 COPY local_settings.py /www/repo_health
 COPY manage.py /www/

 WORKDIR repo_health/index/static
 RUN npm install && npm run dist 
 EXPOSE 8080

 WORKDIR /www
 CMD ["python", "manage.py"]
