
from fastapi import FastAPI , Path , HTTPException , Query
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

@app.get('/patient/{patient_id}')

def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve" , example="P001")):
    # load all the patient 
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
    

@app.get('/sort')
def sort_patients(sort_by: str = Query(... , description='Sort on the basis of height , weight , or bmi') , order: str = Query('asc' , description='sor in asc or desc order')):
    
    valid_fields = ['height', 'weight' , 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400 , detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code = 400, detail='invalid orider select between asc and desc')
    data = load_data()
    sort_order = True if order=='desc' else False
    
    sorted_data = sorted(data.values() , key=lambda x :x.get(sort_by , 0 ), reverse=False)
    
    return sorted_data
    
    