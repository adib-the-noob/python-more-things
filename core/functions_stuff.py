from typing import Tuple

def user_info(*info, **extras):
    print("User Information:", info)
    for key, value in extras.items():
        print(f"{key}: {value}")

user_info("Alice", "Bob", age=30, city="New York")

def calculate(a: int, b: int) -> Tuple[int, int, int]:
    sum_result = a + b
    diff_result = a - b
    product_result = a * b
    return sum_result, diff_result, product_result

add, sub, mul = calculate(10, 5)
print("Sum, Difference, Product:", add, sub, mul)