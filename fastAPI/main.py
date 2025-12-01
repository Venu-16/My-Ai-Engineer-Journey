from fastapi import FastAPI, HTTPException, Path, Query
import json

def load_json():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data

app = FastAPI()

@app.get("/")

def hello_world():
    return {"message": "Hello, World!"}

@app.get("/about")

def about():
    return {"message": "this is Maile Venu Madhav Upcoming ML Enginner"}


@app.get("/view")

def view():
    data = load_json()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_json()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sorted")
def sorted_patients(sortby: str = Query(..., description="sort by height, weight or bmi"), order: str = Query("asc", description ="sort by asc")):
    
    if sortby not in ["height", "weight", "bmi"]:
        raise HTTPException(status_code=400, detail="Invalid sortby parameter select in {'height', 'weight', 'bmi'}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order parameter select in {'asc', 'desc'}")
    
    data = load_json()
    sorted_data = sorted(data.values(), key=lambda x: x[sortby], reverse=(order=="desc"))
    return sorted_data
    