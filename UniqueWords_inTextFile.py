text_file = open ("MyData.txt" , 'r')
text = text_file.read()

 
text = text.lower()

words = text.split()

words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]


unique = [] ## unique words ko isme store krenge 

for word in words:
    if word not in unique:
        unique.append( word)



unique.sort()
sentence = " “Someone on TV has only to say, ‘Alexa,’ and she lights up. She’s always ready for action, the perfect woman, never says, ‘Not tonight, dear.’” "
print(sentence.split(','))
print(unique)


