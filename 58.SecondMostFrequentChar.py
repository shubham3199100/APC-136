s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_chars) > 1:
    print(sorted_chars[1][0])
else:
    print("No second frequent character")
