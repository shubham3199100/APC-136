s1 = input("First string: ").replace(" ", "").lower()
s2 = input("Second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
