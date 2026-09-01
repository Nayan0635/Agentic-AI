# tpl = ()
# s = int(input("Enter size: "))



# # taking names from user
# for i in range(0, s, 1):
#     name = input("give name? ")
#     tpl += (name, )

# # diplay names..
# for t in tpl:
#     print(t)

# # count elements
# print(f"NO of elements: {s}")

# already created
tpl = ('c++', 'python', 'java', 'rust')

# display elements using for loop
cnt = 0
for t in tpl:
    cnt+= 1
    print(f"Name: {t}")
    
# print(len(tpl))
print(f"No of elements: {cnt}")