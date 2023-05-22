# Task 11 - String handling. Read in a string, make alternate character capital, make alternate words capital.

sentence = input("Please enter a sentence of at least three words: ")

while len(sentence.split()) < 3: # Testing for number of words in user input to increase chance of string manipulation working.
    sentence = input("Your sentence appears a bit too short. Please enter a sentence of at least three words: ")

print(f"\n{sentence}\n") # Printing initial string so manipulated srings can be compared easily.

sentence1 = ""

# Iterate to build sentence1 using alternate case characters

for i in range(len(sentence)):
    if i%2 == 0:
        sentence1 += sentence[i].upper()
    else:
        sentence1 += sentence[i].lower()
print(f"{sentence1}\n")

sentence2 = sentence.split(" ")

sentence3 = ""

# Iterate to build sentence3 using alternate case words

for i in range(len(sentence2)):
    if i%2 == 0:
        sentence3 += sentence2[i].upper() + " "
    else:
        sentence3 += sentence2[i].lower() + " "


sentence4 = sentence3.rstrip() # Strip final " ".

print(f"{sentence3}\n") 