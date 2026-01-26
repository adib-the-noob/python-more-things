# chai_order = dict(
#     customer_name="John Doe",
#     order_id=456,
#     items={"chai": 2, "cookies": 5},
#     total_price=29.99
# )
# print(chai_order)

# user_info = {}

# user_info["username"] = "johndoe"
# user_info["email"] = "johndoe@example.com"

# print(user_info)

# del user_info["email"]
# print(user_info)

user_date = {
    "event": "Conference",
    "date": "2024-09-15",
    "location": "New York",
    "attendees": 150
}

print(f"All the keys: {list(user_date.keys())}")
print(f"All the values: {list(user_date.values())}")
print(f"All the items: {list(user_date.items())}")

print("---")
for items in user_date.items():
    print(f"{items[0]} -> {items[1]}")

# Namedtuples
print("--- Namedtuples ---")
from collections import namedtuple

chaiProfile = namedtuple("ChaiProfile", ["name", "spice_level", "milk_type", "sugar_level"])
my_chai = chaiProfile(name="Masala Chai", spice_level="Medium", milk_type="Whole", sugar_level="Low")
print(my_chai)