from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 5:
            raise ValueError('Username must be at least 5 characters long')
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, model):
        if model.password != model.confirm_password:
            raise ValueError('Passwords do not match')
        return model
    

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

# Example usage
if __name__ == "__main__":
    # User validation example
    try:
        user = User(username="john")
    except ValueError as e:
        print(f"User validation error: {e}")

    # SignupData validation example
    try:
        signup_data = SignupData(password="secret123", confirm_password="secret1234")
    except ValueError as e:
        print(f"SignupData validation error: {e}")

    # Product computed field example
    product = Product(price=19.99, quantity=3)
    print(f"Total price for product: {product.total_price}")