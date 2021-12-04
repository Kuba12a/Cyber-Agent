from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import Model.Command as command_model

app = FastAPI()

#TODO Agent na podstawie action musi wykonać u siebie odpowiednią operację
@app.post("/command")
def login(command: command_model.Command):
    print(f"Action type: {command.action}")
    return {"msg": "Command received successfully by the agent"}
