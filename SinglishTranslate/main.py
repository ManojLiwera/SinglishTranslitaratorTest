import nltk
import re
from nltk.corpus import wordnet
import string
import googletrans
from googletrans import Translator
from nltk.corpus import words
import emoji
import http.client
import json

stopwords = open("Stopwords.txt", 'r', encoding='utf-8').read()


def remove_url(comment):
    url_removed = re.sub("(https|http)?:\\\/\\\/+.*[\r\n]*", '', comment)
    return url_removed


def isSinglish(word):
    word = word.lower()
    if(word in words.words()):
        return False
    else:
        if wordnet.synsets(word):
            return False
        else:
            return True


def isEnglish(sentence):
    c = 0
    for w in sentence.split():
        if re.match('[a-zA-Z]', w) is not None:
            c = c+1
    if (c > 1):
        return True
    else:
        return False


def tokenizeLine(line):
    tokens = nltk.word_tokenize(line)
    return tokens


def googleTranslate(line):
    gTrans = Translator()
    a = gTrans.translate(line, dest='si').text
    return a


def remove_punctuations(text):
    without_punc = "".join([c for c in text if c not in string.punctuation])
    return without_punc


def removeStopWords(line):
    tokens = tokenizeLine(line)
    result = [i for i in tokens if not i in stopwords]
    return result

# detect and replace emojis with description


def emojiToText(text):
    allchars = [str for str in text]
    for word in allchars:
        if word in emoji.UNICODE_EMOJI:
            emoji_desc = emoji.demojize(word)
            text = text.replace(word, emoji_desc)
    return text


def removeEmoji(text):
    allchars = [str for str in text]
    for word in allchars:
        if word in emoji.UNICODE_EMOJI:
            emoji_desc = emoji.demojize(word)
            text = text.replace(word, "")
    return text

# translated and demojize statements
# def translatedEmojiText(text):
#     translated_statement = translate_english(text)
#     emoji_desc_statement = text_has_emoji(translated_statement)
#     return emoji_desc_statement


def detect_language(line):
    sinhala = 0
    english = 0
    singlish = 0
    nonAlpha = 0
    hashtags = 0
    other = 0
    line = remove_punctuations(line)
    line = remove_url(line)
    line = removeEmoji(line)
    # tokens = nltk.word_tokenize(line)
    # print(tokens)
    for w in line.split():
        if u'\u0D80' <= w <= u'\u0DFF':
            sinhala = sinhala+1
        elif re.match('[a-zA-Z]', w) is not None:
            if (isSinglish(w)):
                singlish = singlish+1
            else:
                english = english+1
        elif re.match(r'\#', w) is not None:
            hashtags = hashtags+1
        elif re.match(r'[0-9\&\-\.\?\$]', w) is not None:
            nonAlpha = nonAlpha+1
        else:
            other = other+1
    maxWord = max(sinhala, singlish, english, nonAlpha, hashtags, other)
    wordSum = sinhala+singlish+english+nonAlpha+hashtags+other
    if(wordSum == sinhala):
        return "SIN"
    elif(english > singlish and (english > sinhala)):
        return "ENG"
    elif(english <= singlish):
        return "SNG"


def getProbability(word1):
    new_dict = {}
    with open("commentLines\sinhalaComments", encoding='utf-8') as fp:
        for line in fp:
            words = line.split()

            for word in words:
                word = word.lower()

                if word not in new_dict:
                    new_dict[word] = 1
                else:
                    new_dict[word] += 1

    total_words = sum(new_dict.values())
    with open("newpast.txt", 'w', encoding='utf-16') as f:
        # The dictionary is set as: {dictionary_name[key] : value}
        for key, value in sorted(new_dict.items()):
            # probability = value / total_words
            f.write(key + "\n")
    # print(new_dict.get("පිස්සුද"))
    # return new_dict.get(word1) / total_words


def request(input):
    conn = http.client.HTTPSConnection('inputtools.google.com')
    conn.request('GET', '/request?text=' + input +
                 '&itc=si-t-i0-und&num=10&cp=0&cs=1&ie=utf-8&oe=utf-8&app=test')
    res = conn.getresponse()
    return res


# print(str(request("kariya").read(),encoding='utf-8')[14+3+len("kariya"):-48])
# getProbability("පිස්සුද")