#Lab 2

name = "Jonathan Patrick Wells"

#Activity 1
if len(name) > 15:
    print("Your name: " + name + ", is greater than 15 characters")
elif len(name) <= 15 and len(name) >= 10:
    print("Your name: " + name + ". is between 10 and 15 characters")
else:
    print("Your name: " + name + ", is less than 10 characters")

#Activity 2, not sure which way you wanted
nameString = ""
nameString2 = ""
for char in name:
    print(char)
    nameString += char
print("Result of loop: " + nameString)

######
print("")
print("")
######

for i in range(len(name)):
    print(name[i])
    nameString2 += name[i]
print("Result of loop 2: " + nameString2)
    
