

user_input = input("Enter an integer n (press Enter to use default 8): ").strip()
n = int(user_input) if user_input else 8

result = {i: i * i for i in range(1, n + 1)}

print(f"Generated dictionary for n = {n}:")
print(result)

