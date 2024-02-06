# with open("message.txt","a") as fileWrite:
#     # fileWrite.write("Hello From Python\n")
#     fileWrite.write("Again Hello From BRo")


with open("message.txt","r") as fileRead:
    text = fileRead.read()
    print(text)