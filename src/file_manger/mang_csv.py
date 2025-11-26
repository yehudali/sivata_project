from fastapi import UploadFile
import csv
import io


def upload_csv(file: UploadFile):
    """
    Endpoint that extracts and processes a CSV file from the request.
    Uses Python's csv library to read and parse the CSV data.
    """
 
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}
    

   
    content = file.file.read().decode("utf-8")


    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)

    return header,rows

    