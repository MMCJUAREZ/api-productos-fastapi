from pydantic import BaseModel

class SumaRequest(BaseModel):
    a: float
    b: float
