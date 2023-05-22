# sentence = this is a test sentence 

# sentence2 = sentence.split( )
# print(sentence2)
# sentence3 = []

# # Iterate to build sentence3 using alternate case words

# for i in range(len(sentence2)):
#     if i%2 == 0:
#         sentence3.append(sentence2[i].upper()) # adds a word to list?????????
#     else:
#         sentence3.append(sentence2[i].lower())


# print(sentence3)   # is a list of letters????????????
# print( .join(sentence3)) 

#*********************
# import copy
# sdgasSd


# a = [[1, 2, 3], [4, 5, 6]]
# b = [int(elem) for elem in a[0]]

# b.extend(a[1])

# c = b.copy()

# c.extend([3, 5, 3])

# print(a)
# print(b)   # prints none none
# print(c)

# # **************
stock = {"juice" : 5, "coffee" : 9, "pie" : 8, "apple" : 10, "milk" : 3}
print(stock["juice"])
# print(stock.keys()[2])
del stock["juice"]
print(stock)