# Dockerfile.streamlit
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
