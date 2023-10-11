# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get upgrade
RUN apt-get -y update
RUN apt-get install -y pkg-config

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5001 for the Flask app
EXPOSE 5001

# Run the Flask app when the container launches
CMD ["python", "app.py"]