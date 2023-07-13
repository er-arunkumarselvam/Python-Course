# range
rangeOfValues = range(10)
print(rangeOfValues, type(rangeOfValues))
# range print in for loop
for value in range(10):
    print(value, end=" ")
rangeValue = range(5, 20)
print()
for value in rangeValue:
    print(value, end=" ")
print()
valuesOfRange = range(20, 5, -2)  # starting, ending, step
for value in valuesOfRange:
    print(value, end=" ")
print()
ranges = range(5, 50, 2)
print(ranges[0])
print(ranges[2:5])
print(ranges[-1])
# Bytes
priceList = [10, 20, 30, 25]
newPriceList = bytes(priceList)
for value in newPriceList:
    print(value, end=" ")
print(type(newPriceList))
# newPriceList[0] = 100
# print(newPriceList[0])
print()
# Bytearray
priceList = [10, 20, 30, 25]
newPriceList = bytearray(priceList)
print(priceList[0], type(newPriceList))
priceList[0]=100  # Mutable
print(priceList[0])
for value in newPriceList:
    print(value, end=" ")
print(type(newPriceList))
print()