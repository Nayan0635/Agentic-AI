# listen~ Silent
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Sort the characters of each string
str1 = ''.join(sorted(str1))
str2 = ''.join(sorted(str2))

if str1 == str2:
    print("Anagram")
else:
    print("Not Anagram")