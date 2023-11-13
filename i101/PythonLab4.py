import random

##sentence = "Hello, you are looking good today."
##
##sentence = sentence.split()
##
##print(sentence)
##
##sentence[4] = "striking"
##
##print(sentence)
##
##
##def changeString(string):
##    string = string.split()
##    string[1] = input("Change the word at index 1: ")
##    return string
##
##
##for word in sentence:
##    print(word)
##
##newSentence = input("Enter a sentence: ")
##
##newSentence = newSentence.split()

sentence = "Hello, you are looking *adj today."

sentence = sentence.split()

adjectives = ["beautiful", "handsome", "pretty", "warm", "fantastic"]

for i in range(len(sentence)):
    if sentence[i] == "*adj":
        sentence[i] = random.choice(adjectives)

print(sentence)

string = ""
for word in sentence:
    string += word + " "
print(string)

sentence1 = " ".join(sentence)

print(sentence1)
