 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 ENTRYPOINT ["repo-health"]
 LABEL Description="This image supplies the server needed for repo-health."
 
 # Setting up database
 RUN apt-get update && apt-get install -y \
     curl
 RUN curl -O https://ghtstorage.blob.core.windows.net/downloads/msr14-mysql.gz
 RUN gzip -d msr14-mysql.gz
 COPY init_db.sh /www/
 RUN chmod +x /www/init_db.sh && /www/init_db.sh

 RUN mkdir /www
 WORKDIR /www
 COPY ../requirements.txt /www/
 RUN pip install -r requirements.txt
 COPY ../. /www/

 WORKDIR repo_health/index/static
 RUN npm install && npm run dist
 RUN python manage.py migrate
 
 EXPOSE 8080
