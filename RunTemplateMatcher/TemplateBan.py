from SpacyConstants import *

class TemplateBan:

    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer

    def preprocess(self, sentence):
        sentence = sentence.replace('\n','')

        return sentence

    def parse(self, sentence):
    	sentence = self.preprocess(sentence)
        if self.parseTreeUtil.getHeadOfSentence(sentence).text != "banned":
           self.parseNounForm(sentence)
        else:
           self.parseVerbForm(sentence)
   
    def parseVerbForm(self, sentence):
        timePeriod = None
        reason = None
        who = None
        fromWhat = None
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp(sentence)
   
        associatedPrepositionIds = {}
        
        #Find associated Prep Ids and subject
        for token in doc:
            if token.head.i == headToken.i and token.tag_ == SPACY_TAG_PREP:
                associatedPrepositionIds[token.i] = token
            elif token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]):
                who = self.parseTreeUtil.getSubTreeString(token)
                
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text == PREP_FOR :
                    if token.tag_ in [SPACY_TAG_NN, SPACY_TAG_NNS, SPACY_TAG_NNP, SPACY_TAG_NNPS]:     
                        timePeriod = self.parseTreeUtil.getSubTreeString(token)
                    else:
                        reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_FROM:
                    fromWhat = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_UNTIL:
                    timePeriod = self.parseTreeUtil.getSubTreeString(token)
                    
        print(sentence)
        print(" who: ", who,
             " reason :", reason,
             " timePeriod :", timePeriod,"fromWhat:", fromWhat,'\n')
        
    def parseNounForm(self, sentence):
        timePeriod = None
        reason = None
        who = None
        fromWhat = None
        associatedPrepositionIds = {}
        doc = self.spacyNlp(sentence)
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        
        
        for token in doc:       
            tokenLemma = self.wordnetLemmatizer.lemmatize(token.text)
            if tokenLemma == 'ban' or tokenLemma == 'banned':
                banToken = token
            elif token.head.tag_ in [SPACY_TAG_VBN] and token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]):
                who = self.parseTreeUtil.getSubTreeString(token)
            elif token.head.tag_ != SPACY_TAG_VBN and token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_IND_OBJ_1, SPACY_DEP_IND_OBJ_2]):
                who = self.parseTreeUtil.getSubTreeString(token)
        # Fetching preps connected to Ban tag
        for token in doc:
            if token.head.i == banToken.i and token.tag_ == SPACY_TAG_PREP:
                associatedPrepositionIds[token.i] = token
            
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text == PREP_FOR :
                    if token.tag_ in [SPACY_TAG_NN, SPACY_TAG_NNS, SPACY_TAG_NNP, SPACY_TAG_NNPS]:     
                        timePeriod = self.parseTreeUtil.getSubTreeString(token)
                    else:
                        reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_FROM:
                    fromWhat = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_UNTIL:
                    timePeriod = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_TO:
                    who = self.parseTreeUtil.getSubTreeString(token)
            elif token.head.i == banToken.i and token.tag_ in [SPACY_TAG_NN, SPACY_TAG_NNS, SPACY_TAG_NNP, SPACY_TAG_NNPS, SPACY_TAG_JJ,SPACY_TAG_JJR, SPACY_TAG_JJS]:
                timePeriod = self.parseTreeUtil.getSubTreeString(token)
        
        print(sentence)
        print(" who: ", who,
             " reason :", reason,
             " timePeriod :", timePeriod,"fromWhat:", fromWhat,'\n')