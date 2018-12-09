from SpacyConstants import *

class TemplateShare:
    
    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer


    def preprocess(self, sentence):
        sentence = sentence.replace('shares','shows')
        sentence = sentence.replace('share','show')
        sentence = sentence.replace('\n','')

        return sentence

    def getCompoundPhrase(self, sentence, rootTokenId):
         doc = self.spacyNlp(sentence)
         phrase = []
         for token in doc:
             if (token.tag_ != SPACY_TAG_PREP) and (token.head.i == rootTokenId or token.i == rootTokenId):
                 phrase.append(token.text)
         reversed(phrase)
         return ' '.join(phrase)

    def parse(self, sentence):
         doc = self.spacyNlp(sentence)
         whoShared = None
         whoSharedId = None
         
         typeShared = None
         typeSharedId = None
         
         whatShared = None
         whatSharedId = None
         
         prep = None
         prepId = None
         ww = ''
         sentenceHeadToken = self.parseTreeUtil.getHeadOfSentence(sentence)
         sentenceHead = sentenceHeadToken.text
         #print("sent head: ", sentenceHead)
         for token in doc:
             # if token.dep_ == SPACY_DEP_ROOT:
             #     print (sentence, token.text)
             if token.dep_ == SPACY_DEP_NSUBJ and token.head.text == sentenceHead:
                 whoShared = token.text
                 whoSharedId = token.i
             if (token.dep_ == SPACY_DEP_DOBJ or token.dep_ == SPACY_DEP_CCOMP) and token.head.text == sentenceHead :
                 typeShared = token.text
                 typeSharedId = token.i
                 
         #Figuring out preposition for typeShared       
         for token in doc:
             if token.dep_ == SPACY_DEP_PREP and token.head.text == typeShared:
                 prep = token.text
                 prepId = token.i
                 
                 
                 #for token1 in 
                 ww = [str(token1.text) for token1 in list(token.subtree)]
                 break
         if prep != None:
             for token in doc:
                 if token.dep_ == SPACY_DEP_PREP_OBJ and token.head.i == prepId:
                     whatShared = token.text
                     whatSharedId = token.i
         #print(sentence, "who: ", whoShared, "type: ", typeShared, "what: ", whatShared)
         print(sentence)
         print("who: ", self.getCompoundPhrase(sentence, whoSharedId), 
               "type: ", self.getCompoundPhrase(sentence, typeSharedId), 
               #"what: ", getCompoundPhrase(sentence, whatSharedId))
               "what: ", ' '.join(ww))
         print('\n')