# Base image
FROM python:3.10-slim-buster

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set up working directory
WORKDIR /app

# Install project dependencies
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy project code base
COPY . .

# Expose container ports
EXPOSE 80 8000 8080

# Entry points
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]