from pydantic import BaseModel

# pydantic model ma schema define garyo 
class Patient(BaseModel):
    name: str
    age: int
      
def insert_patient_data(patient: Patient):
    #yo duita data database ma rakhnu xa re
    print(patient.name)
    print(patient.age)
    print('inserted successfully')
    #yo duita data database ma rakhnu xa re
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    

Patient_info = {'name': 'shyam', 'age': 30}

patient1 = Patient(**Patient_info) 

# yo pydantic model ko help le data lai validate garxa ani structre ma rakhxa

insert_patient_data(patient1) 
update_patient_data(patient1)
# correct input
# so pydantic use garera easily type validation garna sakinxa ani code pani clean hunxa.