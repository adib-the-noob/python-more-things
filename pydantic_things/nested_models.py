from pydantic import BaseModel
from typing import List, Optional 

class Address(BaseModel):
    steert: str
    city: str
    postal_code: str

class User(BaseModel):
    street: str
    postal_code: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None

Comment.model_rebuild()  # To handle self-referencing models


adrress = Address(steert="123 Main St", city="Anytown", postal_code="12345")
user = User(street="123 Main St", postal_code="12345", address=adrress)

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(id=2, content="This is a reply"),
        Comment(id=3, content="This is another reply", replies=[
            Comment(id=4, content="Nested reply")
        ])
    ]
)
print(user)
print('---')
print(comment)  