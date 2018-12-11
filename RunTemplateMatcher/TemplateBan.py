# Pak's Shehzad banned for 4 months for anti-doping violation
# Cricketer given 20-week ban for physical altercation in match

# WI coach banned from World cup over inappropriate comments

from SpacyConstants import *

class TemplateBan:

    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer
        self.semanticHelper = semanticHelper

    def preprocess(self, sentence):
        sentence = sentence.replace('\n','')

        return sentence

    def parse(self, sentence):
    	sentence = self.preprocess(sentence)
        if self.parseTreeUtil.getHeadOfSentence(sentence).text in ["banned", "bans"]:
           self.parseVerbForm(sentence)
        else:
           self.parseNounForm(sentence)
   
    def parseVerbForm(self, sentence):
        timePeriod = None
        reason = None
        who = None
        fromWhat = None
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp(sentence)
   
        #Find associated Prep Ids and subject
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        
        whoGotBanned = self.findWhoGotBannedInVerbForm(sentence, headToken)
        whoBanned = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))
        for token in doc:
            if token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]):
                who = self.parseTreeUtil.getSubTreeString(token)
                
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text == PREP_FOR :
                    if token.tag_ in [SPACY_TAG_NN, SPACY_TAG_NNS, SPACY_TAG_NNP, SPACY_TAG_NNPS] and self.semanticHelper.isARelationshipExists(token.text, "time_unit"):     
                        timePeriod = self.parseTreeUtil.getSubTreeString(token)
                    else:
                        reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_FROM:
                    fromWhat = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_UNTIL:
                    timePeriod = self.parseTreeUtil.getSubTreeString(token)
                    
        
        print(" whoGotBanned: ", whoGotBanned,
            "whoBanned: ", whoBanned,
             " reason :", reason,
             " timePeriod :", timePeriod,"fromWhat:", fromWhat)
        print('\n')
        
    def parseNounForm(self, sentence):
        timePeriod = None
        reason = None
        who = None
        fromWhat = None
        
        doc = self.spacyNlp(sentence)
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        
#Ronaldo received 1-match ban, clear to face former club Man Utd
        #print(headToken)
        #print(self.parseTreeUtil.printTree())
        whoBanned = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))    
        for token in doc:       
            tokenLemma = self.wordnetLemmatizer.lemmatize(token.text)
            if tokenLemma == 'ban' or tokenLemma == 'banned':
                banToken = token
            elif token.head.tag_ in [SPACY_TAG_VBN, SPACY_TAG_VBZ] and token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]):
                who = self.parseTreeUtil.getSubTreeString(token)
            elif token.head.tag_ != SPACY_TAG_VBN and token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_IND_OBJ_1, SPACY_DEP_IND_OBJ_2]):
                who = self.parseTreeUtil.getSubTreeString(token)
        # Fetching preps connected to Ban tag
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        
            
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text == PREP_FOR :
                    if token.tag_ in [SPACY_TAG_NN, SPACY_TAG_NNS, SPACY_TAG_NNP, SPACY_TAG_NNPS] and self.semanticHelper.isARelationshipExists(token.text, "time_unit"):     
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
        print(" whoWasBanned: ", who,
             " reason :", reason,
             " timePeriod :", timePeriod,"fromWhat:", fromWhat,'\n')

    def findWhoGotBannedInVerbForm(self, sentence, actionToken):
        if actionToken.tag_ in [SPACY_TAG_VB, SPACY_TAG_VBD, SPACY_TAG_VBG, SPACY_TAG_VBP, SPACY_TAG_VBZ]:
            whoGotBanned = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findObjectOfToken(sentence, actionToken))
        else:
            whoGotBanned = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findSubjectOfToken(sentence, actionToken))
        return whoGotBanned











