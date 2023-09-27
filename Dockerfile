FROM python:3.7-slim-buster

# Copy the contents of the Code file to app
ADD . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the environment variable FLASK_APP to app.py
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
