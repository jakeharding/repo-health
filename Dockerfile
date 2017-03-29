 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 LABEL Description="This image supplies the server needed for repo-health."
 
 # Setting up database
 RUN apt-get update && apt-get install -y curl netcat
 RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
 RUN apt-get install -y nodejs
 RUN mkdir /www
 WORKDIR /www

 COPY requirements.txt /www/
 RUN pip install -r requirements.txt
 COPY . /www

 WORKDIR repo_health/index/static
 RUN npm install && npm run dist 
 WORKDIR /www

 EXPOSE 8000

 COPY docker/runserver.sh /runserver.sh
 CMD ["/runserver.sh"]

