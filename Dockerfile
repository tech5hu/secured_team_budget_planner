# using the official Python image
FROM python:3.10

# setting working directory inside container
WORKDIR /app

# copying all code into the container
COPY . /app

# installing Python packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ruunning the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
