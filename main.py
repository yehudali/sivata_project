from fastapi import FastAPI
import uvicorn 
from src.routes.routes import router

from creating_base import creating_base_homes_and_rooms

app = FastAPI()

app.include_router(router)

def play():
    base_sivata=creating_base_homes_and_rooms("sivata",2,10)
    





if __name__=="__main__":
    play()
    uvicorn.run(app , host="localhost", port=8000)