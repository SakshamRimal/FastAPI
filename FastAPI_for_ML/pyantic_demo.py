from pydantic import BaseModel , EmailStr , Field
from typing import List, Dict , Optional

# pydantic model ma schema define garyo 
class Patient(BaseModel):
    name: str = Field(..., min_length=2 , max_length=50) # yo name ko lagi ho
    age: int = Field(..., gt=0) # yo age ko lagi ho greater than 0
    email: EmailStr # yo email ko lagi ho
    weight: float = Field(..., gt=0 , lt=300) # yo weight ko lagi ho greater than 0 and less than 300
    married: bool
    allergies: Optional[List[str]] = None# list matra validate garnu xaina bhitra string xa ki nai ni garnu parxa so we use List 
    contact_details: Dict[str , str] # in this too same 
      

def insert_patient_data(patient: Patient):
    #yo duita data database ma rakhnu xa re
    print(patient.name)
    print(patient.age)
    print('inserted successfully')
    #yo duita data database ma rakhnu xa re
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    

Patient_info = {'name': 'shyam', 'age': 30 ,
                'email': 'abc@gmail.com' ,
                'weight':72.2 , 
                'married': True , 
                'allergies':['pollen' , 'dust'] ,
                'contact_details':{'phone': '223344'}
}


patient1 = Patient(**Patient_info) 

# yo pydantic model ko help le data lai validate garxa ani structre ma rakhxa

insert_patient_data(patient1) 
update_patient_data(patient1)
# correct input
# so pydantic use garera easily type validation garna sakinxa ani code pani clean hunxa.