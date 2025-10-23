from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
 
# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fb-backend-dpgacwh3ckc5gbad.centralindia-01.azurewebsites.net/"],  # we'll tighten this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}
 
@app.get("/api/hello")
def hello(name: str = "Reshmika"):

    return {"greeting": f"Hello, {name}! Welcome to FastAPI"}


