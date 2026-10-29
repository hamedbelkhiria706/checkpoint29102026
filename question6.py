 
print("--- 1. Creating a set ---")
my_set = {0, 1, 2, 3, 4}
print("Created set:", my_set)

 
print("\n--- 2. Iterating over the set ---")
for item in my_set:
    print("Item:", item)

 
print("\n--- 3. Adding and removing items ---")
sample_set = {"apple", "banana", "cherry"}
print("Initial set:", sample_set)

 
sample_set.add("orange")                
sample_set.update(["mango", "grape"])    
print("After adding members:", sample_set)

 
sample_set.remove("banana")             
sample_set.discard("kiwi")              
popped_item = sample_set.pop()          

print(f"Removed item via pop(): {popped_item}")
print("Final set after removals:", sample_set)

