from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):

    model_config = {"from_attributes": True}
    
    access_token: str
    token_type: str