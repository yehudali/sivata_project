from fastapi import APIRouter
from src.file_manger.mang_csv import upload_csv

router = APIRouter()



@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/assignWithCsv")
def soldier_deployment(file):
    header,rows=upload_csv(file)
    for line in rows:
        print(line)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "total_rows": len(rows),
        "columns": header,
        "data": rows[0:5],
        "message": f"Successfully processed CSV with {len(rows)} rows"
}