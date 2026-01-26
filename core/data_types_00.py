# sets
essential_spices = {"salt", "pepper", "cumin", "paprika"}
optional_spices = {"oregano", "basil", "thyme", "cumin"}

all_spices = essential_spices | optional_spices # union of two sets 
# all_spices.union(optional_spices) -> union using method 

common_spices = essential_spices & optional_spices # intersection of two sets
# common_spices = essential_spices.intersection(optional_spices) -> intersection using method

print("All spices:", all_spices)
print("Common spices:", common_spices)

# Checking any specific element of one set is in another set
print(f"Is 'cumin' an essential spice? {'cumin' in essential_spices}")

# Frozensets
frozen_spices = frozenset(["nutmeg", "clove", "cardamom"])
print("Frozen spices:", frozen_spices)