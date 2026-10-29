 

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sample List:", sample_list)


sample_list.sort(key=lambda x: x[-1])

print("Expected result:", sample_list)

