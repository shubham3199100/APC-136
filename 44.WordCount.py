s = input("Enter a sentence: ")
count=1
#words = s.split()
#print("Number of words:", len(words))

for i in s:
    if i==" ":
        count+=1

print("WordCount:",count)
    
