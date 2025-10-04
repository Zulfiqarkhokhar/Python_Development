# for loop

for i in range(5):
    print(f"Hi {i}")

## range(start,stop) (inclusive, exclusive)
    
for i in range(2,8):
    print(f"Bye {i}")

## range(start,stop,step) (inclusive, exclusive,step)
    
for i in range(10,20,2):
    print(i)

word = "Zulfiqar"

for char in word:
    print(char.split(" "))


# while loop 

num = 0

while num<5:
    print(num)
    num+=1

password =""

while len(password)<=8:
    password = input("please enter password more than 8 character: ")

print("thanks")


