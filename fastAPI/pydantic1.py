from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    alergies: Optional[List[str]] - None
    contact_details : Dict[str,str]



def insert_patient_data(name,age):

    print(name)
    print(age)
    print("inserted into db")

insert_patient_data("venu","twenty")

patient_info = {"name": "venu", "age":21, "weight":60.0}

p1 = Patient(**patient_info)

insert_patient_data(p1)
