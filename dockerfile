# Use full Python base image (not slim)
FROM python:3.10

# Avoid caching and unnecessary files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the entire app code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI server using Python module syntax
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
