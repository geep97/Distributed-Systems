from fastapi import APIRouter
from pydantic import BaseModel



router =   APIRouter(tags = ["jobs"])


class JobStub(BaseModel):
    job_type : str
    payload : str



@router.get(
    "/jobs",)

def jobs( ):
    return  [{"job_id":1,"status" :"queued"},
             {"job_id":2,"status" :"processing"},
             {"job_id":3,"status" :"failed"},]



@router.get("/jobs/{job_id}")
def look_jobs(job_id:int):
    return {
        "job_id": job_id,
        "status": "queued",

    }


@router.post("/jobs",)
def create_job(job:JobStub):
    return {

        "job_type": job.job_type,
        "payload": job.payload,
        "job_id": 99, "status": "queued"

    }
