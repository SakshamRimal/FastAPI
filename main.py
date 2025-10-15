from fastapi import FastAPI

app = FastAPI()

@app.get("/")
# route create gareko decorator ko help le 

# then method define gareko for the particular route
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")

def about():
    return {"message": "This is the about page."}

