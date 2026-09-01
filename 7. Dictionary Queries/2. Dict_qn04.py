# Assignment 1: Product Database

products = [
{"id":1,"name":"Laptop","price":55000,"qty":10},
{"id":2,"name":"Mouse","price":700,"qty":50},
{"id":3,"name":"Keyboard","price":1200,"qty":40},
{"id":4,"name":"Monitor","price":14000,"qty":12},
{"id":5,"name":"Headphone","price":2500,"qty":25}
]

# Tasks
# Find products costing more than  10,000/- XXX
print("Product costing more than 10000 : ")

for prod in products:
    if prod["price"] >= 10000:
        print(f"{prod["name"]} : {prod["price"]}")
print()


# Calculate inventory value (price × qty) for each product.XXX

def inventory_value(prod: dict):
    price = prod.get("price")
    qty = prod.get("qty")
    
    inven_value = price*qty
    
    # return {"inventory value" : inven_value}
    return {**prod, "inventory value" : inven_value}
    
Products = list(map(inventory_value, products))

# for prod in products:
#     inventory = inventory_value(prod)
#     print(inventory)

for item in Products:
    print(f"{item["name"]} : {item["inventory value"]}")
    


# Find the product having maximum inventory value.XXX
print("\nMaximum Inventory Value Product: ")
# def maximunInvent(prod):
#     maxi = max(prod.get(""))

sorted_inventory = sorted(Products, key = lambda x : x["inventory value"], reverse= True)
print(sorted_inventory[0]["name"], sorted_inventory[0]["inventory value"])




# Sort by price.XXX
print("\nSorted by Price: ")
# def sort_price(itemObj: dict):
#     return itemObj.get("price")
# sorted_byPrice = sorted(products, key = sort_price)
# print(sorted_byPrice)

sorted_byPrice = sorted(products, key = lambda x: x["price"])
for item in  sorted_byPrice:
    print(item["name"], item["price"])



# Sort by quantity.XXX
print("\nSorted by Qty: ")

# def sort_qty(itemObj: dict):
#     return itemObj.get("qty")
# sorted_byPrice = sorted(products, key = sort_price)
# print(sorted_byQty)

sorted_byQty = sorted(products, key = lambda x: x["qty"])
for item in  sorted_byQty:
    print(item["name"], item["qty"])



# Find total inventory value.XXX

def total_inventory(product):
    total_price = 0
    for item in product:
        total_price+= item.get("price")
    return total_price

total = total_inventory(products)
print("\nTotal Inventory: ", total, end="\n")



# Find products whose names contain the letter 'o'XXX
print("Products containing letter 'o': ")

def product_name(produc):
    for product in products:
        if 'o' in product.get("name").lower():
            print(product.get("name"))

product_name(products)