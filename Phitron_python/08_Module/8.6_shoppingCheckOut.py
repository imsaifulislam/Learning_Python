class Shopper:
    
    """ def __init__(self,name):
        self.name = name
        self.cart = [] """
    
    def __init__(self):
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item' : item, 'Price': price, 'Quantity': quantity})
        
    def chackOut(self,amount):
        price = 0
        for items in self.cart:
            print(items)
            price += items['Price'] * items['Quantity']
        
        # print(price)
        if amount<price:
            return f"Please Give me More Money: {price-amount} Taka"
        elif amount>price:
            return f"Here are The Items andd Extra Money : {amount-price} Taka"
        else:
            return 'Here are the items'

# shopping = Shopper('Febrilife')
shopping = Shopper()
shopping.add_to_cart('Shirt',400,3)
shopping.add_to_cart('pant',1400,2)
shopping.add_to_cart('Shoes',899,4)

reply = shopping.chackOut(8000)
print(reply)