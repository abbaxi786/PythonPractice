# Build a shopping cart that supports adding and removing items (using a list). 

cart = ["lentil","grains","wheat","eggs"]

def addCart(arr,itemToBeAdded):
     arr.append(itemToBeAdded)
     return arr
    
def RemoveItem(arr,itemToBeRemoved):
    arr.remove(itemToBeRemoved)
    return arr

addItem = input("Enter the item you want to add: ")

cart = addCart(cart,addItem)

print(f"The item is add to {addItem} to the cart {cart}")

removeItem = input("Enter the item you want to remove: ")


cart = RemoveItem(cart, removeItem)

print(f"{removeItem} is remove from the cart {cart}")
