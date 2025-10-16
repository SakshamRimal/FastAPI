
def insert_patient_data(name ,age):
    #yo duita data database ma rakhnu xa re
    if(type(name) != str):
        raise ValueError("Name must be a string")
    if(type(age) != int):
        raise ValueError("Age must be an integer")
    else:
        return True
    
insert_patient_data('ram' , 25) # correct input

# here we expected that age to be integer but we are passing string
# so to avoid this we use pydantic

# ya pani sacalable option haina validation ta hunxa but code badi hunxa dherai parameter bhayo bhane sabai ko lagi if else lekhnu parxa ani dherai lamo hunxa.
