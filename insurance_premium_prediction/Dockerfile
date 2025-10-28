#base image
FROM python:3.10

# working directory
WORKDIR /app

#copy requirements file
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . /app/
EXPOSE 8000

CMD ["uvicorn" , "app:app" , "--host" , "0.0.0.0" , "--port" , "8000"]