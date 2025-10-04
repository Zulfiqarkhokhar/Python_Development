# tuples are ordered but immutable collection of elements

my_tuple = (1,4,2,5,"hello",False)

print(my_tuple)

print(my_tuple[4])

print(type(my_tuple))

#my_tuple[2] = "banana" # not allow due to immutable

new_tuple = my_tuple +(3,"banana")

print(new_tuple)  