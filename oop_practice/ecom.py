class Product:
    
    def __init__(self, name, product_id, price, stock) -> None:
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock = stock
    
    def update_stock(self,amount):  
        if self.stock == 0:
            self.stock = amount
        else:
            self.stock += amount
    
    def get_product_info(self):
        return f'Name: {self.name} Product ID: {self.product_id} Price: {self.price} Stock: {self.stock}'
    
    def apply_discount(self, am):
        dis = (100-am)/100
        self.price = dis *self.price
        
p1 = Product('Laptop', 101, 1000, 50)
p2 = Product('Phone', 102, 3000, 20)

print(p1.get_product_info())
p2.apply_discount(10)
print(p2.get_product_info())



