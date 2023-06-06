# Set
details = {"Arun", 24, True }
print(details)
print(type(details)) # <class 'set'>
details = {"Prasanna", 24, True, 24} # Duplicates not allowed
print(details)
details.add("Civil Engineer")
print(details)
details.remove(24)
print(details)
details.pop() # current first index is removed
print(details)
print(details.pop()) # return value
# Dictionary
values = {}
print(type(values)) # <class 'dict'>
# Using Operators
name1 = {"Arun", "Kumar", "Selvam"}
name2 = {"Prasanna", "Praveen", "Selvam"}
print(name1 - name2) # Only First Set values
print(name1 | name2) # Either or set1 or set2 (Union)
print(name1 & name2) # Intersection value only
print(name1 ^ name2) # Only one value
#program
details = {"Arun", 24, True, 5.11}
for values in details:
    if isinstance(values, int):
   # if type(i) is int:
        print(values)
