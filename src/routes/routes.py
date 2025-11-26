from fastapi import APIRouter

router = APIRouter()



@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/assignWithCsv")
def soldier_deployment():
    
    return {"message": "root "}