from SpacyConstants import *

class TemplateTweets:

    def __init__(self, spacyNlp, parseTreeUtil):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil

    def preprocess(self, sentence):
        sentence = sentence.replace('tweets','says')
        sentence = sentence.replace('\n','')

        return sentence

    def parse(self, sentence):
        sentence = self.preprocess(sentence)
        who = ""
        whoToken = None
        tweet = ""
        tweetToken = None
        context = None
        
        saysToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp(sentence)
        for token in doc:
            if token.head.i == saysToken.i and token.i != saysToken.i: 
                #print(token.text)
                if token.dep_ == SPACY_DEP_NSUBJ:
                    who = (token.text)
                    whoToken = token
                else:
                    tweet += self.parseTreeUtil.getSubTreeString(token)
                    
        if whoToken != None:
            for token in doc:
                if token.tag_ == SPACY_TAG_PREP and token.head.i == whoToken.i:
                    context = self.parseTreeUtil.getSubTreeString(token)
        print(sentence)           
        print("Who: ",who,"; Tweet: ",tweet," Context: ", context,'\n')


# Dhoni knew about Rafale, tweets user on Dhoni's T20I exclusion