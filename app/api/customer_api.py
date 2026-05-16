from fastapi import APIRouter

from app.models.customer import  CustomerQuery
from app.services.customer_service import get_customer

router = APIRouter()

@router.post("/customers/query")
def query_customer(data: CustomerQuery):

    return get_customer(data.customer_name)