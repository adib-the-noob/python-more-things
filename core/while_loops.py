i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    if i == 4:
        break
    print(f"Current value of i: {i}")

print("===" * 10)

staff = [
    ("John", "Manager"),
    ("Jane", "Developer"),
    ("Doe", "Designer"),
]

for member, role in staff:
    print(f"{member} is a {role}")

print("===" * 10)

while (line := input()) != "":
    print("You typed:", line)
