""" class Employee:
    # -> Class Variable
    companyName = "Apple"
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(
            f"{self.noOfEmployee} The Name of Employee is {self.name} & the Raise Amount in {self.companyName} is {self.raise_amount}")


Employee.companyName = "Google"
print(Employee.companyName)

emp1 = Employee("Shanto")
emp1.showDetails()

# -> Instanve Variable
emp2 = Employee("Saiful")
emp2.raise_amount = .25
emp2.companyName = "Apple Bangladesh"
emp2.showDetails() """


""" 
    * যদি Instanve Variable কোন ভেরিএবল এর ডাটা পরিবর্তন করা হয় তাহলে অব্জেট সেইটা পাবে আর যদি Instanve Variable না পায় তাহলে Class Variable এর থেকে ডাটা নিবে
    * https://replit.com/@SaifulIslamShan/66-Day-66-Instance-vs-Class-variables
    
    * ইনস্ট্যান্স ভ্যারিয়েবল (Instance Variables):
        -> ইনস্ট্যান্স ভ্যারিয়েবল হলো ক্লাসের প্রতিটি অবজেক্টের সাথে সংযুক্ত হয়। অন্তর্ভুক্ত ভ্যারিয়েবলগুলি সাধারণভাবে ক্লাসের init মেথডে সেট করা হয়। ইনস্ট্যান্স ভ্যারিয়েবলগুলি অবজেক্টের প্রতিটি অনুক্রিয়ামান অ্যাট্রিবিউট হিসেবে কাজ করে। একটি অবজেক্ট এর ইনস্ট্যান্স ভ্যারিয়েবলগুলি অন্তর্নিহিত মান রাখতে সক্ষম।
        
    * ক্লাস ভ্যারিয়েবল (Class Variables):
        -> ক্লাস ভ্যারিয়েবল হলো সকল অবজেক্টের মধ্যে শেয়ার হওয়া ভ্যারিয়েবল যা ক্লাসের সাথে সংযুক্ত হয়। ক্লাস ভ্যারিয়েবলগুলি ক্লাসের সাথে সংজ্ঞায়িত হয় এবং সকল অবজেক্ট এই সাধারণ ভাবে একই মান রাখে। একটি অবজেক্ট এর ক্লাস ভ্যারিয়েবলে কোন পরিবর্তন করলে এটি সমস্ত অবজেক্টের জন্য পরিবর্তন হয়।
"""


""" class car:

    vehicle = "car"

    def __init__(self, weight, color):
    
        # -> Instance Variable
        self.weight = weight
        self.color = color


civic_2015 = car(1247, "red")
print(civic_2015.weight)
print(civic_2015.color) """


# -> ClassVariable

""" class myClass:
    class_variable = 0
    
    def __init__(self):
        myClass.class_variable +=1
    
    def print_class_Variabel(self):
        print(myClass.class_variable)

obj1 = myClass()
obj2 = myClass()

obj1.print_class_Variabel()
obj2.print_class_Variabel() """


""" class Student:
    def __init__(self, name, roll):
        # -> Instance Variable
        self.name = name
        self.roll = roll


Student1 = Student("Shanto", 53)
Student2 = Student("Liza", 101)

print(Student1.name)
print(Student2.roll) """


#* classVariable
class circle:
    
    # ->ClassVariable
    pi = 3.1416
    
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return circle.pi * self.radius * self.radius
    
circle1= circle(5)
circle2= circle(7)

print(circle1.area())
print(circle2.area())

""" 
    * আমরা Circle নামের একটি ক্লাস তৈরি করেছি এবং এটির ভিতরে আমরা pi নামে একটি ক্লাস ভ্যারিয়েবল সেট করেছি। এটির মান সকল অবজেক্টের মধ্যে শেয়ার হয় এবং এটি Circle.pi দ্বারা অ্যাক্সেস করা যায়। আমরা অবজেক্টের মাধ্যমে area() মেথড কল করতে পারি, যা ক্লাস ভ্যারিয়েবল pi এর মান ব্যবহার করে পরিস্কার করে। 
    
    * ইনস্ট্যান্স ভ্যারিয়েবল অবজেক্ট বা ইনস্ট্যান্সের জন্য একক মান রাখে যেখানে ক্লাস ভ্যারিয়েবল সমস্ত অবজেক্টের জন্য একই মান রাখে এবং তা সমস্ত অবজেক্টের মধ্যে শেয়ার হয়।
"""