from fastapi import APIRouter



router =   APIRouter(tags = ["jobs"])

@router.get(
    "/jobs",)




def jobs(  ):
    return  [{"id":1,"status" :"queued"},
             {"id":2,"status" :"processing"},
             {"id":3,"status" :"failed"},]


