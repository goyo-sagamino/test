import random as ran
file = open('text.txt','r')
text = file.read()
text = text.splitlines()
print(text)
file.close()
