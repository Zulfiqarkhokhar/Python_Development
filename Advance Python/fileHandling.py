# info = open("users.txt",mode="r")
# print(info.name)
# print(info.readable())

# user_info = open("data.txt","w") # create the file if not available

# # writing to file

# user_info.write("Hello bro I am python dev")

# friends = ["Idrees\n","mitho\n","Irfan\n"]

# user_info.writelines(friends)

# user_info = open("data.txt","r")

# print(user_info.read())
# print(user_info.readline())

# copy data

data = open("data.txt","r")
copy = open("copy.txt","w")

content = data.read()

copy.write(content)

