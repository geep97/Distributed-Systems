from fastapi import APIRouter
from pydantic import BaseModel



router =   APIRouter(tags = ["jobs"])


class JobStub(BaseModel):
    status : str
    job_id : int



@router.get(
    "/jobs",)

def jobs(  ):
    return  [{"id":1,"status" :"queued"},
             {"id":2,"status" :"processing"},
             {"id":3,"status" :"failed"},]



@router.get("/jobs/{job_id}")
def look_jobs(job_id:int):
    return {
        "job_id": job_id,
        "status": "queued",

    }


@router.post("/jobs",)
def create_job(job:JobStub):
    return {
        "job_id": job.job_id,
        "status": job.status

    }
