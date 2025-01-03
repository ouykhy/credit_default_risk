# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (if any required)
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
&& rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry==1.6.1

# Configure Poetry to not create virtual environments
RUN poetry config virtualenvs.create false

# Copy only pyproject.toml and poetry.lock to leverage Docker cache
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app/

# Expose port (optional, as Heroku manages routing)
EXPOSE 8000

# Command to run the FastAPI app, binding to the PORT provided by Heroku
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]