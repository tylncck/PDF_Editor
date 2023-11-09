FROM python:3.9

WORKDIR /app

USER root

# Copy requirements.txt file onto your image
COPY /requirements.txt /

# Install system-level dependencies, upgrade pip, and install Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    ghostscript && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip setuptools wheel && \
    pip install -r /requirements.txt
