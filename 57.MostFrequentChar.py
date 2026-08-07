s = input("Enter string: ")

max_char = max(set(s), key=s.count)
print(max_char)
