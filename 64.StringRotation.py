s1 = input("First string: ")
s2 = input("Second string: ")

if len(s1) == len(s2) and s2 in s1 + s1:
    print("Yes")
else:
    print("No")
