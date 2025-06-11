# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install flask mysql-connector-python

# Expose Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]