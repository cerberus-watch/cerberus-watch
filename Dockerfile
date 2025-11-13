# Stage 1: Builder - Install dependencies
FROM python:3.11-slim-bookworm AS builder

# Set working directory
WORKDIR /opt/venv

# Create a virtual environment
RUN python -m venv .

# Activate the virtual environment and install dependencies
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install --no-cache-dir -r requirements.txt


# Stage 2: Final - Create the production image
FROM python:3.11-slim-bookworm AS final

# Create a non-root user and group
RUN groupadd --system appuser && useradd --system --gid appuser appuser

# Set working directory
WORKDIR /home/appuser/app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY --chown=appuser:appuser . .

# Set the PATH to include the venv
ENV PATH="/opt/venv/bin:$PATH"

# HEAD_NAME will be set at runtime by docker-compose.yml
# e.g., ENV HEAD_NAME=template

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Run the application with Gunicorn using the shell form of CMD
# This allows the ${HEAD_NAME} environment variable to be expanded.
CMD gunicorn -w 2 -k uvicorn.workers.UvicornWorker "heads.${HEAD_NAME}.main:app" --bind 0.0.0.0:8000
