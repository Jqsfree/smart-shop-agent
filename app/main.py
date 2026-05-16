from fastapi import FastAPI
from app.api.customer_api import  router as customer_router



app = FastAPI(
    title="Smart Shop Agent",
    version="0.1.0",
)





@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Agent Running"}

app.include_router(customer_router)