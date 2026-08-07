paragraph = input("Enter paragraph: ")

freq = {}

for word in paragraph.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
