# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV MYSQL_HOST="mysql_host"
ENV MYSQL_USER="mysql_user"
ENV MYSQL_PASSWORD="mysql_password"
ENV MYSQL_DB="analytics_data"

# Run app.py when the container launches
CMD ["python", "app.py"]