s = input("Enter string: ")
seen = set()

for ch in s:
    if s.count(ch) > 1 and ch not in seen:
        print(ch)
        seen.add(ch)
