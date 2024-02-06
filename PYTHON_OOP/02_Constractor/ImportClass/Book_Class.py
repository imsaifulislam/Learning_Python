class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.price = 0
    
    """ 
        * => Set Method Update 
        * => Get Method show Update
    """
    def set_price(self,price):
        self.price = price
    
    def get_price(self):
        return self.price
    
    def details(self):
        print(f"Book Name: {self.name}\nAuthor Name: {self.author}\nPrice: {self.price} Taka")
        
# =========================================================

