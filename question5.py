 
data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print("Original list:", data)

 
sorted_data = sorted(data, key=lambda x: float(x[1]), reverse=True)

print("Expected result:", sorted_data)

