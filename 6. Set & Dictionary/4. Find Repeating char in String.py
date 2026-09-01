# s = input("Enter the string: ")
s = "kjgfkuhf"
dct = {}

for ch in s:
    dct.update({ch : s.count(ch)})
    
# print(dct)

for ch in s:
    if dct[ch] == 1:
        print(f"First non Repeating char: {ch}")
        break

for ch in s:
    if dct[ch] >= 2:
        print(f"First Repeating char: {ch}")
        break
    
max_key = None
maxi = float('-inf')

# maxi = max(dct.values())

for key, value in dct.items():
    # if value > maxi:
    #     maxi = value
    #     max_key = key
    max_key = max(dct, key = dct.get)

print(f"Maximum frequency key : {max_key}")