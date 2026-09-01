
def product_name(empObj: dict):
    for item in empObj:
        if 'o' in empObj.get("name"):
            return empObj.get("name")

onamed_products = list(product_name, products)
for item in onamed_products:
    print(item["name"])