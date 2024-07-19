from pydantic import BaseModel

class Application_Schema(BaseModel):

    kind: str = None
    name: str = None
    description: str = None
    version: str = None
    configuration: dict = None
    settings: dict = None