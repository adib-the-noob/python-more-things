from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    name: str = Field(
        ..., alias="cart_name", min_length=3, examples=["My Cart", "Shopping List"]
    )
    quatities: Dict[str, int]
    amount: Optional[float] = Field(ge=1, description="Total amount in the cart")

# Example usage
if __name__ == "__main__":
    cart_data = {
        "user_id": 123,
        "items": ["apple", "banana", "orange"],
        "cart_name": "Grocery Cart",
        "quatities": {"apple": 2, "banana": 3, "orange": 1},
        "amount": 15.75
    }
    
    cart = Cart(**cart_data)
    print(cart)
    