class customerInfo:
    def __init__(self,orderId, name, phonenumber, amount):
        self.id = orderId
        self.name = name
        self.number = phonenumber
        self.OrderAmount = amount
        
    def showInfo(self):
        print(f"Order Id: {self.id}\nName : {self.name}\nNumber : {self.number}\nOrder Amount: {self.OrderAmount}")


class cutomerDB:
    def __init__(self):
        self.customers = []
    
    def add_customer(self,customer):
        self.customers.append(customer)
    
    def get_customer_info(self,target_orderId):
        for customer in self.customers:
            if customer.id == target_orderId:
                return f"CUstomer info from search\nOrder Id: {self.id}\nName : {self.name}\nNumber : {self.number}\nOrder Amount: {self.OrderAmount}"
            else:
                return "Customer not found in the Database"

                


customer1 = customerInfo(orderId=1, name="Alice", number="555-1234",amount=100)
customer2 = customerInfo(orderId=2, name="Alice", number="555-1234",amount=100)
customer3 = customerInfo(orderId=3, name="Alice", number="555-1234",amount=100)

customer_Db = cutomerDB()
customer_Db.add_customer(customer1)
customer_Db.add_customer(customer2)
customer_Db.add_customer(customer3)

# customer3.showInfo()

target_orderId = 2
result = customer_Db.get_customer_info(target_orderId)
print(result)



""" class Customer:
    def __init__(self, orderId, name, amount, number):
        self.orderId = orderId
        self.name = name
        self.amount = amount
        self.number = number

class CustomerDatabase:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer_info(self, target_orderId):
        for customer in self.customers:
            if customer.orderId == target_orderId:
                return f"Customer Info: OrderID={customer.orderId}, Name={customer.name}, Amount={customer.amount}, Number={customer.number}"
        return "Customer not found in the database"

# Example usage:

# Create instances of the Customer class
customer1 = Customer(orderId=1, name="Alice", amount=100, number="555-1234")
customer2 = Customer(orderId=2, name="Bob", amount=150, number="555-5678")
customer3 = Customer(orderId=3, name="Charlie", amount=200, number="555-9876")

# Create a CustomerDatabase and add customers to it
customer_database = CustomerDatabase()
customer_database.add_customer(customer1)
customer_database.add_customer(customer2)
customer_database.add_customer(customer3)

# Search for customer information using orderId
target_orderId = 2
result = customer_database.get_customer_info(target_orderId)
print(result)
 """