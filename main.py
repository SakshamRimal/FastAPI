
from fastapi import FastAPI , Path , HTTPException , Query
from pydantic import BaseModel , Field , computed_field 
from fastapi.responses import JSONResponse
from typing import Annotated , Literal , Optional
import json

app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str , Field(... , description='id of the patient', examples=['P001'])]
    name: Annotated[str , Field(..., description='Name of patient' , examples=['Ram'])]
    city: Annotated[str , Field(...,description='city where the paitent is living')]
    age : Annotated[int , Field(... , gt=0 , lt=120 , description='Age of patient')]
    gender: Annotated[Literal['male' , 'female' , 'others'], Field(... , description='gender of the patient')]
    height: Annotated[float , Field(...,gt=0 , description='height of the pateint')]
    weight: Annotated[float , Field(... , gt=0 , description='Weight of the patient')]
    
    
    # hamro feild exsiting field bata naya banauna milxa
    @computed_field
    @property 
    def bmi(self) -> float:
        bmi = round((self.weight/ self.height**2),2)
        return bmi
        
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'UnderWeight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obesse'

        
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
    
        

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('patient.json' , 'w') as file:
        json.dump(data ,file)
        
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
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    return sorted_data
    
# new endpoint named creatder=='desc' else False
    
    sorted_data = sorted(data.values() , key=lambda x :x.get(sort_by , 0 ), reverse=False)
    
    return sorted_data
    
# new endpoint named create esma chai POST method use garne ani data pani pathaune so
# client le server ma request post method use garera garxa then we validate the data using pydantic if the data is validated then we send the data.

@app.post('/create')
def create_patient(pateint: Patient):
    
    # load the exsiting data 
    data = load_data()
    
    # check if the pateint already exist or not 
    if pateint.id in data:
        raise HTTPException(status_code=400 , detail='Pateint already exist')

    # if new patient add to the database 
    data[pateint.id] = pateint.model_dump(exclude= ['id'])
    
    # save into the json file 
    
    save_data(data)
    
    return JSONResponse(status_code=201 , content={'messagee':'pateint created sucessfully'})

# CRUD operation ma create ra retrieval bhaisakuo aba baki update and delete opertion garne 

# first update or edit garna ko lagi update garna PUT use garnu parxa.

@app.put('/edit/{patient_id}')

def update_patient(patient_id:str , patient_update: PatientUpdate):
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_data_info = data[patient_id]
    
    update_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key , value in update_patient_info.items():
        existing_data_info[key] = value 
        
     #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_data_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_data_info)
    #-> pydantic object -> dict
    existing_data_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_data_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})

    