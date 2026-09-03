from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.router import r



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    #allow_credentials=True,
    allow_methods=["*"],
)




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.head("/")
def read_root():
    return {"Hello": "World"}
