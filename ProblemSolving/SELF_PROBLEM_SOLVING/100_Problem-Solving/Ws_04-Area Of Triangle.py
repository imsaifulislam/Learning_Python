""" base = int(input("Enter base: "))
height = int(input("Enter Height: "))

area = (base*height)/2
print("Area Of Triangle: ",area) """

def areaOfTriangle(x,y):
    area = (x*y)/2
    return area

base = float(input("Enter base: "))
height = float(input("Enter Height: "))

areaIs = areaOfTriangle(base,height)
print("Area Of Triangle: ",areaIs)
