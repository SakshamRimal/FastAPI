from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
# route create gareko decorator ko help le 

# then method define gareko for the particular route
def hello():
    return {"message": "Patient Management System "}

@app.get("/about")

def about():
    return {"message": "Fully functional API to manage patient records."}

# endpoint banaue aba anii json file load garne

@app.get('/view')
def view():
    data = load_data()
    return data