from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
_fake_db = []
class Application_Schema(BaseModel):

    kind: str
    name: str
    description: str
    version: str
    configuration: dict
    settings: dict

@app.post("/application_schema/", response_model=Application_Schema)
def create_application_schema(item: Application_Schema):
    _fake_db.append(item)
    return item

@app.get("/application_schema/{item_id}", response_model=Application_Schema)
def read_application_schema(item_id: int):
    if item_id >= len(_fake_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="Application_Schema not found")
    return _fake_db[item_id]

