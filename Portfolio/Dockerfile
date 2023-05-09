	# Use an official Python runtime as a parent image
	# Use an official Python runtime as a parent image
	FROM python:3.11-slim-buster
	# Set the working directory to /app
	WORKDIR /app
	# Copy the current directory contents into the container at /app
	COPY . /app
	# Install any needed packages specified in requirements.txt
	RUN pip install --upgrade pip
	RUN pip install --trusted-host pypi.python.org -r requirements.txt
	# Make port 8000 available to the world outside this container
	EXPOSE 8000
	# Set the environment variable
	ENV NAME World
	# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

