from pydantic import BaseModel

class CustomerQuery(BaseModel):
    customer_name: str
