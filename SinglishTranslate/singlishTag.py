import main
import pickle
import nltk
import re
import TranslaterLogic
from nltk import PerceptronTagger 
from nltk.corpus import TaggedCorpusReader
from nltk.tag import str2tuple, tuple2str
from nltk.corpus import state_unionUTF
from itertools import product
from sklearn.metrics import classification_report

uni_tagger = open("unigram_tagger.pickle", "rb")
utagger = pickle.load(uni_tagger)

trainSetPath = "E:\\FYproject\\preprocess\\SinglishTranslate\\singlishtrain.txt"

train_text = state_unionUTF.raw(trainSetPath)

testData = []
trainData = []
fTrn = open("E:\\FYproject\\preprocess\\Tagger\\train.txt",
            mode='r', encoding='utf-8')
fTst = open("E:\\FYproject\\preprocess\\Tagger\\test.txt",
            mode='r', encoding='utf-8')

for i in fTrn.readlines():
    trainData.append([str2tuple(t) for t in i.split()])

# [[('Palayan/{පලයන්', 'VNM}'), ('pottaya/{පොට්ටය', 'NNN}'), ('boru/{බොරු', 'JJ}'), ('nokiya/{නොකියා', 'NNM}')],

for i in fTst.readlines():
    testData.append([str2tuple(t) for t in i.split()])


def ngramTranslater(train_sents, n, defaultTag='NN'):
    t0 = nltk.DefaultTagger(defaultTag)
    if (n <= 0):
        return t0
    elif (n == 1):
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        return t1
    elif (n == 2):
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        return t2
    else:
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        t3 = nltk.TrigramTagger(train_sents, backoff=t2)
        return t3

# tra =ngramTranslater(trainData,1)
# print(tra.evaluate(testData))
def writeTag():
    write = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish11.txt",
                 mode='w', encoding='utf-8')
    read = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish1.txt",
                mode='r', encoding='utf-8')
    for i in read:
        singlish = i.split()
        sinhala = next(read).split()
        for n in range(len(singlish)):
            write.write(singlish[n]+"/"+sinhala[n]+" ")
        write.write("\n")
#############################################

###############################################
# def translatorsave():
#     translator = ngramTranslater(trainData, 3, 'NNN')
#     print('Trigram Translator Accuracy : ' + str(translator.evaluate(testData)))
#     save_translator = open("SinglishTranslate\\trigramTrans.pickle", "wb")
#     pickle.dump(translator, save_translator)
#     save_translator.close()

translateorPic = open("trigramTrans.pickle", "rb")
translator = pickle.load(translateorPic)
def triGramTranslate(sentence):
    translation = ""
    translated = translator.tag(nltk.word_tokenize(sentence.lower()))
    for word, trans in translated:
        if trans in ('NNN'):
            translation = translation+str(TranslaterLogic.convertText(word)+" ")
        else:
            translation = translation+str(trans+" ")
    return translation

def onlytriGramTranslate(sentence):
    translation = ""
    translated = translator.tag(nltk.word_tokenize(sentence.lower()))
    for word, trans in translated:
        translation = translation+str(trans+" ")
    return translation

    # tagged_test_sentences = tagger.tag_sents([[token for token, tag in sent] for sent in testData])
    # gold = [str(tag) for sentence in testData for token, tag in sentence]
    # prediction = [str(tag) for sentence in tagged_test_sentences for token, tag in sentence]
    # print(metrics.classification_report(gold, prediction))


def uniTagger():
    tagger = ngramTagger(trainData, 1, 'NNN')
    print('Unigram Accuracy : ' + str(tagger.evaluate(testData)))
    print(tagger.tag(nltk.word_tokenize("eka nam hondai")))


def translate(sentence):
    translated = []
    tokened = nltk.word_tokenize(sentence)

    for word in tokened:
        matched = getMatch(word)
        translated.append(matched)
    print(translated)
    unigramtag(translated)


def getMatch(testWord):
    possiblities = []
    splitted = nltk.word_tokenize(train_text)
    for word in splitted:
        pureWord, singlishWord = word.split("/")

        if (testWord == pureWord):
            if (singlishWord in possiblities):
                continue
            else:
                possiblities.append(singlishWord)
    if(len(possiblities) == 0):
        possiblities.append("--")
    return possiblities

# tagger_t = open("perceptron_tagger.pickle", "rb")
# tagger = pickle.load(tagger_t)


def unigramtag(sentence):
    for word in sentence:
        print(utagger.tag(word))


def tagAndTranslate(translatedList):
    semtenceList = list(product(*translatedList))


# uniTagger("palayan boru karaya yanna tho muslim eka oya Ehema habaya arabi endumak nam kota gawmath brithanya endumak")
# print(triGramTranslate("today mama yanwa uba")
# [['එක'], ['නම්'], ['හොන්දයි', 'මොනවා']]
# translate("eka nam hondai mama yanawa")

# writeTag()
# translatorsave()


def translatorAcuracy():
    read = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish2.txt",
                mode='r', encoding='utf-8')
    Nwronng = 0
    Nright=0
    N=0
    for i in read:
        singlish = onlytriGramTranslate(i).split()
        sinhala = next(read).split()
        N=N+len(singlish)
        for n in range(len(singlish)):
            if(singlish[n] == sinhala[n]):
                Nright = Nright +1
            else:
                Nwronng = Nwronng+1
    
    print(N,Nwronng,Nright,Nright/N)

def ruleTranslate():
    read = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish2.txt",
                mode='r', encoding='utf-8')
    Nw = 0
    Nr=0
    Nn=0
    for i in read:
        singlish = TranslaterLogic.convertText(i).split()
        sinhala = next(read).split()
        Nn=Nn+len(singlish)
        for n in range(len(singlish)):
            if(singlish[n] == sinhala[n]):
                Nr = Nr +1
            else:
                Nw = Nw+1
    print(Nn,Nw,Nr,Nr/Nn)
def confusionmat():
    sin =[]
    sig=[]
    read = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish2.txt",
                mode='r', encoding='utf-8')
    for i in read:
        singlish = triGramTranslate(i).split()
        sinhalatext = next(read)
        sinhala=sinhalatext.split()
        for n in range(len(singlish)):
            sin.append(sinhala[n])
            sig.append(singlish[n])
    classification_report(sin,sig)
def acuracyletterWiseTranslate():
    read = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish2.txt",
                mode='r', encoding='utf-8')
    Nw = 0
    Nr=0
    Nn=0
    for i in read:
        singlish = triGramTranslate(i).split()
        sinhalatext = next(read)
        sinhala=sinhalatext.split()
        Nn= Nn+len(re.findall(r'\w\W?',sinhalatext))
        for n in range(len(singlish)):
            if(singlish[n] == sinhala[n]):
                Nr=Nr+ len(re.findall(r'\w\W?',sinhala[n]))
            else:
                singlishleters=re.findall(r'\w\W?',singlish[n])
                sinhalaleters=re.findall(r'\w\W?',sinhala[n])
                if(len(singlishleters)==len(sinhalaleters)):
                    for ns in range(len(sinhalaleters)):
                        if(singlishleters[ns]==sinhalaleters[ns]):
                            Nr=Nr+1
                        else:
                            Nw=Nw+1
                elif(len(singlishleters) > len(sinhalaleters)):
                    for ns in range(len(sinhalaleters)):
                        if(singlishleters[ns]==sinhalaleters[ns]):
                            Nr=Nr+1
                        else:
                            Nw=Nw+1
                else:
                    for ns in range(len(singlishleters)):
                        if(singlishleters[ns]==sinhalaleters[ns]):
                            Nr=Nr+1
                        else:
                            Nw=Nw+1
    print(Nn,Nw,Nr,Nr/Nn)
# print(re.findall(r'\w\W?', "මොකෙක්ද යකො තෝ තොගෙ බොරු අපි නම් දන්නව හිපාටුව තොගෙ ඇස් පේන්නෙ නැත්තන් පාඩුවේ ඉදපන්"))
# print(triGramTranslate("aththenma eda mama giya gedara adanam yanne na"))
ruleTranslate()
translatorAcuracy()
acuracyletterWiseTranslate()
# print(TranslaterLogic.convertText("Ane yaman ballo Pacha kelinda apa yako"))
# print(translator.tag(nltk.word_tokenize("Ane yaman ballo Pacha kelinda apa yako")))
# # print(triGramTranslate("Ane yaman ballo Pacha kelinda apa yako"))
# confusionmat()


