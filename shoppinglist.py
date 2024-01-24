shoppinglist=[]
def add(shoppinglist,item,price):
    shoppinglist.append((item,price))
for i in range(3):
    item=input("Enter product name: ")
    price=input("Enter product price: ")
    add(shoppinglist,item,price)
    print(shoppinglist)
    
def total(shoppinglist,price):
    Sum=sum(shoppinglist)
    print(Sum)
print(total) 