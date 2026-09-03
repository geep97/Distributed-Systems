from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.router import jobs






app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    #allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(jobs.router)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.head("/")
def read_root():
    return {"Hello": "World"}
