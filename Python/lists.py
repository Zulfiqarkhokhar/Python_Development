# list are unorder but mutable 
# creating list

nums = [1,2,3,4,5,6,7,8,9]

print(nums)
print(type(nums))

for i in nums:
    print(i)


print(f"lenght of nums list {len(nums)}")

fruits = ['apple','banana','orange']

print(fruits)

mixed = [1,'apple',3.14,True]

print(mixed)

for i in mixed:
    print(i)

print(mixed[2])

print(mixed[-3])

# slicing

my_list = [1,2,3,4,5,6]
subset = my_list[1:4]
print(subset)

if subset == my_list[1:4]:
    print("True condition")

left_list = my_list[:3]

print(left_list)
right_list = my_list[3:]
print(right_list)

# update list

my_list[2] = "Two"

print(my_list)

# deleting or remove

del my_list[2]

print(my_list)

my_list.remove(4)

print(my_list)