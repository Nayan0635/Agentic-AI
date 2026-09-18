from langchain_core.tools import tool

weight_units = {
    "g" : 1,
    "kg" : 1000,
    "pound" : 453.59,
    "ounce" : 28.35
}


@tool
def weight_converter(value, from_unit, to_unit):
    '''to convert weight "from_unit" to "to_unit"..'''
    
    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()
    
    if from_unit not in weight_units:
        raise ValueError(f"Unknown Unit: {from_unit}")
    if to_unit not in weight_units:
        raise ValueError(f"Unknown Unit: {to_unit}")
    
    grams = value * weight_units[from_unit]
    return grams/weight_units[to_unit]

currency_units = {
    "INR" : 1,
    "USD" : 95.79,
    "YUAN" : 14.30,
    "DIRHAMS" : 26.08,
    "POUND" : 127.98,
    "EURO" : 110.13,
    "RIAL" : 249.37,
}

@tool
def currency_converter(value, from_unit, to_unit):
    '''to convert currency "from_unit" to "to_unit"..'''
    
    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()
    
    if from_unit not in currency_units:
        raise ValueError(f"Unknown Unit: {from_unit}")
    if to_unit not in weight_units:
        raise ValueError(f"Unknown Unit: {to_unit}")
    
    grams = value * weight_units[from_unit]
    return grams/weight_units[to_unit]

@tool
def budget_calculator(price, tax_rate, budget):
    '''to calculate tax/budget'''
    
    tax =  price * tax_rate
    cost = price + tax
    
    report = {
        "price" : price,
        "tax" : tax,
        "total" : cost,
        "remaining" : budget - cost if cost <= budget else 0.0,
        "over by" : cost - budget if cost > budget else 0.0
    }
    p, t, c = report["price"], report["tax"], report["total"]
    
    print(f"Price: ₹{p:,.2f}")
    print(f"Tax ({tax_rate}%): ₹{t:,.2f}")
    print(f"Total: ₹{c:,.2f}")
    
    if report["remaining"]:
        return f'''✅Fits! You'll have ₹{report["remaining"]:, .2f} left.'''
    else:
        return f'''❌Over budget by ₹{report["over by"]:, .2f}.'''