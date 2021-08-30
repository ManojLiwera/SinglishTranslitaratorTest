import nltk
words = []
read = open("E:\\FYproject\\preprocess\\Tagger\\taggerSen.txt",mode='r', encoding='utf-8')
for i in read.readlines():
    for t in i.split():
        if (t in words):
            continue ;
        else:
            words.append(t)

def returnMinEditWord(mistake,distance):
    if(mistake in words):
        correct = mistake
    else: 
        for word in words:
            if(nltk.edit_distance(mistake, word) ==distance and len(mistake)<=len(word)):
                print(word)
    
    return correct
returnMinEditWord("කරය",2)