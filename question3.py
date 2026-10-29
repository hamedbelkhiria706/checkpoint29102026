

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print("d1:", d1)
print("d2:", d2)


result = d1.copy()
for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print("Expected result:", result)

