# Use official Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set the command to run the script
CMD ["python", "app.py"]
