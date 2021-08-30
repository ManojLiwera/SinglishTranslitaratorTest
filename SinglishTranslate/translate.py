import json
import TranslaterLogic
from spellchecker import SpellChecker
import main
import untag

# spell = SpellChecker(language=None)
# spell.word_frequency.load_text_file("E:\\FYproject\\preprocess\\Tagger\\taggerSen.txt",encoding="utf-8")
# spell.export("E:\\FYproject\\preprocess\\SinglishTranslate\\fre.txt")

# spell1 = SpellChecker(language=None, local_dictionary="E:\\FYproject\\preprocess\\SinglishTranslate\\fre.txt")
# spell1.unknown("කරය")
# print(spell1.correction("කරය"))
# print(spell1.candidates("කරය")) 

# write = open("E:\\FYproject\\preprocess\\SinglishTranslate\\t.txt",mode='w', encoding='utf-8')
# read = open("E:\\FYproject\\preprocess\\commentLines\\singlish.txt",mode='r', encoding='utf-8')
# for i in read.readlines():
#     i =main.remove_url(i)
#     i=main.removeEmoji(i)
#     translated = TranslaterLogic.convertText(i)
#     print(translated)
#     write.write(i+translated+"\n")

# write = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish2.txt",mode='w', encoding='utf-8')
# read = open("E:\\FYproject\\preprocess\\SinglishTranslate\\singlish1.txt",mode='r', encoding='utf-8')
# for i in read.readlines():
#     text = main.remove_punctuations(i)
#     if(u'\u0D80' <= str(text) <= u'\u0DFF'):
#         write.write(untag.tagg(text)+"\n")
#     else:
#         write.write(text)