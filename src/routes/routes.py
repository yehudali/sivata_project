from fastapi import APIRouter, UploadFile
from src.file_manger.mang_csv import upload_csv
from ...creating_soldiers import creat_obj_by_file
from ..logic.settlement_management import order_soldiers_by_distance




router = APIRouter()



# @router.get("/")
# async def root():
#     return {"message": "Hello World"}


@router.post("/assignWithCsv")
def soldier_deployment(file: UploadFile):
    header,rows=upload_csv(file)
    list_obj_soldeir=creat_obj_by_file(rows)
    List_of_soldiers_sorted_by_distance=order_soldiers_by_distance(list_obj_soldeir)

    # #test:
    # print("header:", header," rows: ",rows)

    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "total_rows": len(rows),
        "columns": header,
        "data": rows[0:5],
        "message": f"Successfully processed CSV with {len(rows)} rows"
}