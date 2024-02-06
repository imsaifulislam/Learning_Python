class myClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # * instance Method
    def avg(self):
        print((self.a+self.b)/2)


m1 = myClass(20, 30)
m1.avg()
