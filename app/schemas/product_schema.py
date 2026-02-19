from pydantic import BaseModel

class ProductResponse(BaseModel):

    model_config = {"from_attributes": True}

    id: int
    name: str
    price: int
    quantity: int