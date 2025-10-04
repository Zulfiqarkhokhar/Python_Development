# append()
myList = [1,2,3,4]
myList.append(5)
print(myList)

# extend

myList.extend([6,7])

print(myList)

# insert

myList.insert(1,8)

print(myList)

# remove

myList.remove(8)
print(myList)

# pop()
myList.pop()
print(myList)

myList.pop(3) # index
print(myList)

# sort

unsort = [7,1,9,3,8,2]

unsort.sort()

print(unsort)

# copy()

unsort_copy = unsort.copy()

print(unsort_copy)


numbers = [1,2,3,4,5]

# unpacking list

a,b,c,d,e = numbers

print(a,b,c,d,e)

# rest

one,two,*rest = numbers

print(one)
print(two)
print(rest)

