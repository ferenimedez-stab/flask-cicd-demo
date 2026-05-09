# Lightweight official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caches this layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the Flask port
EXPOSE 5000

# Start the app
CMD ["python", "-m", "app.main"]
