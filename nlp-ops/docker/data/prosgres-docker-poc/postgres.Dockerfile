# Use the official PostgreSQL image
FROM postgres:latest

# Set environment variables for default PostgreSQL setup
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin123
ENV POSTGRES_DB=mydatabase

# Expose the PostgreSQL port
EXPOSE 5432
