from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    created_at: datetime
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="John Doe",
    email="jhonedoe@gmail.com",
    address=Address(street="123 Main St", city="Anytown", postal_code="12345"),
    created_at=datetime(2024, 1, 1, 12, 0, 0),
    tags=["admin", "user"],
)

# model_dump()
python_dict = user.model_dump()
print("Python dict representation:")
print(python_dict)

# model_dump_json()
json_str = user.model_dump_json()
print("\nJSON string representation:")
print(json_str)
