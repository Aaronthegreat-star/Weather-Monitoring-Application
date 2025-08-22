# This creates a docker file from a base image of python:alpine3.21
FROM python:3.13-alpine AS builder

#This sets the working directory to /src
WORKDIR /src

# This adds the necessary libraries for the app to run
RUN apk add --no-cache libffi-dev gcc musl-dev

# This copies the requirements file to the container
# COPY requirements.txt .

 #This copies the requirements file to the container
# RUN pip install --no-cache-dir -r requirements.txt

#This installs the uvicorn ASGI server
RUN pip install --no-cache fastapi uvicorn python-dotenv motor pydantic

# This copies the rest of the app source code to the container
COPY Humidity.py ./

# This is used to create the multi-stage build
FROM python:3.13-alpine

# Working directory is set to /src
WORKDIR /src

# The intial stage is called builder and the source code is copied from the builder stage to the current stage
COPY --from=builder /src /src

# This removes the unnecessary libraries that were used to build the app in the builder stage
# RUN apk del libffi-dev gcc musl-dev

#This installs the uvicorn ASGI server
RUN pip install --no-cache fastapi uvicorn python-dotenv motor pydantic


# This deletes the unnecessary libraries that were used to build the app in the builder stage
# RUN apk del gcc libffi-dev musl-dev


# This creates a new user called aaron and changes the ownership of the /src directory to the aaron user
RUN adduser -D aaron  && chown -R aaron:aaron /src/

#This copies the rest of the app source code to the container
# COPY ./ /src/
# The user that will run the app is set to aaron
USER aaron 


# This exposes the port that the app will run on
EXPOSE 8000

# This sets the environment variable for the app to run
# CMD ["uvicorn",  "Humidity:app", "--host", "0.0.0.0", "--port", "8000"] 
ENTRYPOINT ["uvicorn", "Humidity:app", "--host", "0.0.0.0", "--port", "8000"]
