def pour_chai(n):
    if n == 0:
        return "All chai poured"
    return pour_chai(n - 1)

x = pour_chai(5)
# print(x) # This will print "All chai poured"

add_1 = lambda x: x + 1
result = add_1(10)
print("Result of lambda add_1(10):", result)