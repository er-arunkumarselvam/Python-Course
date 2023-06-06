# Dictionary
details = {"Arun":52, "Prasanna":78}
print(details)
details["Arun"]=98
print(details)
details["Balaji"]=75
print(details)
del details["Arun"]
print(details)
print()
# Typecasting of compound datatype
print(list(details))
print(set(details))
print(tuple(details))
print()
# Extract from keys() and values() separated
print(details.keys()) # o/p : dict_keys(['Prasanna', 'Balaji'])
print(details.values()) # o/p : dict_values([78, 75])
# Extract from keys() and values() separated using * operator
print([*details.keys()]) # o/p : ['Prasanna', 'Balaji'']
print([*details.values()]) # o/p : [78, 75]
# get()
employeeDetails = {"name": "Arunkumar", "age" : 24, "Address" : "Ammachatram", "CGPA" : 7.54}
print(employeeDetails.get("CGPA"))
print(employeeDetails.get("city"))
# pop() & popitem()
print(employeeDetails.pop("Address"))
print(employeeDetails)
print(employeeDetails.popitem())
print(employeeDetails)
print()
# Print keys and values for using for loop
employeeDetails = {"name": "Arunkumar", "age" : 24, "Address" : "Ammachatram", "CGPA" : 7.54}
for key in employeeDetails:
    print(key , type(key))
for value in employeeDetails:
    print(employeeDetails[value] , type(value))
print()
# items()
employeeDetails = {"name": "Arunkumar", "age" : 24, "Address" : "Ammachatram", "CGPA" : 7.54}
for key in employeeDetails.items():
    print(key , type(key))