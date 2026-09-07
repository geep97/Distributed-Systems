from fastapi import APIRouter,Depends
from pydantic import BaseModel
from repositories.queue_repository import (create_new_job,list_jobs,get_job)
from core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession


router =   APIRouter(tags = ["jobs"])


class JobStub(BaseModel):
    job_type : str
    payload : dict



@router.get(
    "/jobs",)

async def jobs(db: AsyncSession = Depends(get_db)):
   return await (list_jobs(db))



@router.get("/jobs/{job_id}")
async def look_jobs(job_id:int,db:AsyncSession = Depends(get_db)):
    return await get_job(db, job_id)

@router.post("/jobs",)
async def create_job(job:JobStub,db:AsyncSession = Depends(get_db)):
    return await create_new_job(db, job.job_type, job.payload)
