from fastapi import FastAPI, File, UploadFile, HTTPException
import os
from typing import Any, List,Dict
app = FastAPI()


# change url accordingly
UPLOAD_FOLDER = "D:\TIE\Backend\FAST_API_ENV"
UPLOAD_FOLDER=os.path.join(UPLOAD_FOLDER, "uploads")

def create_folder(folder_name):
    folder_path = os.path.join(UPLOAD_FOLDER, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

@app.post("/upload")
async def upload_image(client_name:str,Bilty_No:str, file: UploadFile = File(...)):

    folder_path = create_folder(client_name)
    print(file.filename)
    # change file name on basis of extension
    # file.filename=file.filename+Bilty_No
    file_path = os.path.join(folder_path, file.filename)

    with open(file_path, "wb") as image:
        image.write(file.file.read())

    return {"message": "Image uploaded successfully", "file_path": file_path}



