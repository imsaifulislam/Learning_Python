class user:
    
    def __init__(self,name,password,phone):
        self.name = name
        self.__password = password
        self.__phone = phone

    def __get_password(self):
        print(self.__password)
        
    def user_log(self,name,password):
        if (name == self.name and password == self.__password):
            return True
        return False 

shanto = user("Shanto","cbvgbdbdvs","01710561898")
# print(shanto.__password)
# shanto.__get_password()
# print(shanto.__phone)

result = shanto.user_log("SHanto","ABCDEDF") 
result = shanto.user_log("Shanto","cbvgbdbdvs") 
print(result)