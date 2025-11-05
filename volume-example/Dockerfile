# using official python image as a base
FROM python:3.12-slim

# set the working directory to be /app
WORKDIR /app

# copy requirements.txt into the working directroy (/app) for pip to install
COPY requirements.txt .

# run command inside container using RUN
# install all the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN is use for building apps, not for running apps

# copy the source code into the directory
COPY src/ .

# expose the port 5000 (flask's default) for runtime
EXPOSE 5000

# the default behaviour (the command that will run) when the container starts
# there can be only one CMD instruction per Dockerfile
# the last one takes effect when multiple are present
CMD ["flask", "run", "--host=0.0.0.0"]
