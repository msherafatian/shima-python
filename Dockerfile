# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12.16
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copy and install requirements first (for better caching)
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Install SHIMA as a package in the container
RUN python -m pip install --no-cache-dir .
# Create sessions directory with proper permissions
RUN mkdir -p /app/sessions && \
    chown -R appuser:appuser /app && \
    chmod 755 /app/sessions

# Switch to non-root user
USER appuser

EXPOSE 8050

# Run with gunicorn
CMD ["gunicorn", "app:server", "--bind=0.0.0.0:8050", "--workers=4", "--timeout=120"]