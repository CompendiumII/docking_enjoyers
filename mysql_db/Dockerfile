FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password1
ENV MYSQL_DATABASE=analytics_data
ENV MYSQL_USER=user1
ENV MYSQL_PASSWORD=password1
ADD init.sql /docker-entrypoint-initdb.d/
EXPOSE 3306