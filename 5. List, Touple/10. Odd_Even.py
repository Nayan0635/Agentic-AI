# x = int(input("Enter the number: "))

# if x/2 == 0:
#     print(f"{x} is Even")
# elif x == 0:
#     print(f"{x} idle number")
# else:    print(f"{x} is Odd")



lst = [2, 4, 2, 16, 19, 7, 6]

maxi_even = lst[0]
mini_even = lst[0]

highest = lst[0]
second_highest = lst[0]



for i in range(len(lst)):
    
    if lst[i]%2 == 0: #even number
        if lst[i] > maxi_even:
            maxi_even = lst[i]
        elif lst[i] < mini_even:
            mini_even = lst[i]
            
    if lst[i] > highest:
        highest = lst[i]
    elif lst[i] > second_highest and lst[i] <= highest:
        second_highest = lst[i]
        
print(f"highest even is  {maxi_even}")
print(f"lowest even is  {mini_even}")
        