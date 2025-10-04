# create function

def greet():
    print("Aslam Alaikum")

greet() 

def printSum():
    sum = 2+3
    print(sum)

printSum()


# function parameter

def addNums(x,y):
    print(x+y)

addNums(3,7)

def greet_user(username):
    print(f"hello {username}")

greet_user("Zulfiqar")


#defaul params

def greet_person(name,msg="Hello"):
    print(f"{name} {msg}")

greet_person("Zulfiqar")
greet_person("Zulfiqar","Salam")

# named arguements

def cal_area(length,width):
    area = length*width
    print(area)

cal_area(length=5,width=10)

cal_area(width=3, length=10)

# return statement

def mul_nums(a,b):
    return a*b

print(mul_nums(10,12))

def square_and_cube(x):
    square = x*x
    cube = x*x*x
    return square,cube

square,cube = square_and_cube(3)

print(square)
print(cube)


# nested functions

def outer_func(x):
    def inner_func(y):
        return x+y
    result = inner_func(5)
    return result

result_val = outer_func(10)

print(result_val)


# lamda function

add = lambda x,y:x+y
result = add(10,50)

print(result)

# callback function

def apply_op(x,y,operation):
    return operation(x,y)
sum = apply_op(5,3,add)

print(sum)