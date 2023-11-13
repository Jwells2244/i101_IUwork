#Lab Python 3

import random


storyList = ["Once","upon","a","time","Magic"]

outputStatem = ""
for val in storyList:
    userInput = input("Add a word to the story as a string: ")
    while type(userInput) != str:
        userInput = input("Add a word to the story as a string: ")
    outputStatem = outputStatem + " " + userInput + " " + random.choice(storyList)
print("Here is your story: ")
print(outputStatem)

print("")
print("")
print("")

print("Now, we do that again but you get to remove a word from the list of words that are given")
print(storyList, ", Here is the list you can remove a word from here.")

wordRemove = input("Enter a word to remove that you see in the list: ")
while wordRemove not in storyList:
    wordRemove = input("Enter a word to remove that you see in the list: ")
storyList.remove(wordRemove)

print("Now we redo the story")

outputStatem = ""
for val in storyList:
    userInput = input("Add a word to the story as a string: ")
    while type(userInput) != str:
        userInput = input("Add a word to the story as a string: ")
    outputStatem = outputStatem + " " + userInput + " " + random.choice(storyList)

print("Here is your story: ")
print(outputStatem)
