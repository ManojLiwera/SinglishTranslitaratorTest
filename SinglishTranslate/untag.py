from nltk.tag import str2tuple, tuple2str, untag
from nltk.tag.perceptron import PerceptronTagger
import pickle
import re
import nltk
import main

tagger_t = open("Tagger\\perceptron_tagger.pickle", "rb")
tagger_save = pickle.load(tagger_t)

def untagging(string):
    untag =""
    for t in string:
        untag = untag+tuple2str(t)+" "
    return untag
def tagg(sentence):
    tagged=tagger_save.tag(nltk.word_tokenize(sentence))
    return untagging(tagged)
# tagger = PerceptronTagger()
# taging = open("commentLines\\englishComments.txt",mode='r', encoding='utf-8')
# print("AAAAAA")
# for i in taging.readlines():
#     tagged=tagger.tag(nltk.word_tokenize(i))
#     print(untagging(tagged))

# # write = open("commentLines\\sinhalaTagged.txt",mode='w', encoding='utf-8')
# # write = open("commentLines\\sinhalaTaggedStemmed.txt",mode='w', encoding='utf-8')
# write = open("commentLines\\sinhalaTaggedStemmedSwRe.txt",mode='w', encoding='utf-8')
# taging = open("Tagger\\taggerSen.txt",mode='r', encoding='utf-8')
# for i in taging.readlines():
#     tagged=tagger_save.tag(nltk.word_tokenize(i))
#     # write.write(untagging(tagged)+"\n")
#     stemmed = stem.stemm_replace(untagging(tagged))
#     write.write(stemmed+"\n")

# # tagger = ngramTagger(trainData,1,"NN")
# # print(tagger.tag(nltk.word_tokenize("තොපිට ඔවා කියන්න පුලුවන්නම් ලන්කාවට වෙන විනාශ නවත්වන්න පුලුවන්නේ")))
# string = [('අඩෝ', 'NNN'), ('බණ්ඩා', 'NNN'), ('උඹට', 'PRP'), ('ආයෙ', 'NNN'), ('කියන්න', 'VNM'), ('නෑ', 'RP'), ('ඔව්වා', 'PRP'), ('වල', 'POST'), ('මිල', 'NNN'), ('දාපන්', 'VNM'), ('අපිටත්', 'NNM'), ('ගිහිල්ලා', 'VP'), ('කන්න', 'VNM'), ('හුත්තේ', 'JJ'), ('හුත්තා', 'NNN'), ('මිල', 'NNN'), ('දාපං', '.')]
# untag =""
# for t in string:
#     untag = untag+tuple2str(t)+" "
# print(untag)
# # print(untag(string))