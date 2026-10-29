 

def multiply_list(items):
    total = 1
    for num in items:
        total *= num
    return total

sample_list = [2, 3, 6]
result = multiply_list(sample_list)

print("Sample list:", sample_list)
print("Result:", result)

