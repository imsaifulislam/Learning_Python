class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num+n

    @staticmethod #-> Decorator
    def add(a, b):
        return a+b


a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)

print(a.add(7, 2))
print(Math.add(7, 2))

# result = Math.add(10, 20)
# print(result)


""" class MathUtils: #-> Class
    @staticmethod
    def add_number(a, b): #-> StaticMethod
        return a+b


result = MathUtils.add_number(5, 10)
print(result)
 """
