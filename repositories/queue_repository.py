from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.job_model import Job


async def list_jobs(db: AsyncSession):
    statement = select(Job)
    result = await db.execute(statement)
    return result.scalars().all()


async def create_job(db:AsyncSession, job_type:str,payload:dict):
    new_job = Job(type=job_type,payload=payload)

    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)

    return new_job


async def get_job(db: AsyncSession, job_id: int):
    statement = select(Job).where(Job.id == job_id)
    result = await db.execute(statement)
    return result.scalars().first()