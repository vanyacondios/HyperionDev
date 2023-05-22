# Compulsory task 2 - Save string. Print without "!". Print in uppercase. Print in reverse
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
print(sentence.replace("!", " "))
# However above leaves a space before the full stop. Should this be unwanted, then
print(sentence.replace("!", " ").strip(" .") + ".")
# I noticed on the group chat you can multiply (call?) more than one function to a string.
print(sentence.replace("!", " ").upper().strip(" .") + ".")
# The task is not explicit on whether the original or a manipulated sentence should be printed in reverse, so
print(sentence[::-1])
# Alternatively
print("." + sentence.replace("!", " ").strip(" .")[::-1])