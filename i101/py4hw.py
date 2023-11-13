import random



sentence = "I'm open to trying anything on campus, and I hope I can make a lot of *adj memories here at *noun University."

sentence = sentence.split()

adjectives = ["beautiful", "handsome", "pretty", "warm", "fantastic"]
nouns = ["beach", "giraffe", "pirate", "baseball", "friend"]


for i in range(len(sentence)):
    if sentence[i] == "*adj":
        sentence[i] = random.choice(adjectives)
    elif sentence[i] == "*noun":
        sentence[i] = random.choice(nouns)

sentence1 = " ".join(sentence)

print(sentence1)
