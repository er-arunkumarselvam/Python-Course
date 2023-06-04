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