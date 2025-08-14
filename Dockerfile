# # Use official Python image
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy project files
# COPY . .

# # Install the package using setup.py
# RUN pip install --upgrade pip
# RUN pip install -e .

# # Expose Flask port
# EXPOSE 5000

# # Start Flask app
# CMD ["python", "app/main.py"]




# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -e .

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
