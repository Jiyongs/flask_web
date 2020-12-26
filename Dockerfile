# Dockerfile
# without an file extension
# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory in the container to /app
WORKDIR /flask_web

# Add the current directory to the container as /app
ADD ./requirements.txt /flask_web/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD ./connect_mongodb.py /flask_web/
ADD ./flask_template.py /flask_web/

# Run flask_template.py when the container launches
CMD ["python", "flask_template.py"]