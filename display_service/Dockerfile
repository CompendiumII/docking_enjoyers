# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory within the container
WORKDIR /app

# Copy your application code into the container
COPY . .

# Install application dependencies
RUN npm install

# Expose the port that your Node.js application will listen on
EXPOSE 3000
EXPOSE 5006

# Command to run your Node.js application
CMD ["node", "app.js"]
