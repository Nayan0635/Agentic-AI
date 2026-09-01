# listen~ Silent
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = ''.join(sorted(str1)) # join sorted(str) with empty ''
str2 = ''.join(sorted(str2))


if str1 == str2:
    print("Anaram")
else:
    print("Not Anaram")
    

