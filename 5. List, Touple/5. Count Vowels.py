word = input("Enter the word: ")
vowels = ['a', 'e', 'i', 'o', 'u']

v= []
c= []
cnt_v = 0
cnt_c = 0

for letter in word:
    if letter in vowels:
        cnt_v+= 1
        v.append(letter)
    else:
        cnt_c+= 1
        c.append(letter)
        
        
print("No of vowels: {} & Number of consonents {}".format(cnt_v, cnt_c))
print(*v)
print(*c)