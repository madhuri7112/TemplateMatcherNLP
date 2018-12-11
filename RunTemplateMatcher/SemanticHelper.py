from SpacyConstants import *
from ConceptNetConstants import *
from ConceptNet import ConceptNet

class SemanticHelper:

    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer
        self.conceptNet = ConceptNet()

    def findAgentOfAction(self, sentence, actionToken):
        agent = None
        subject = self.parseTreeUtil.findSubjectOfToken(sentence, actionToken)
        senObject = self.parseTreeUtil.findObjectOfToken(sentence, actionToken)

        if actionToken.tag_ in [SPACY_TAG_VB, SPACY_TAG_VBD, SPACY_TAG_VBG, SPACY_TAG_VBP, SPACY_TAG_VBZ]:
            agent = subject
        #else:
        # 	# Validate if object is agent
        #     agent = senObject
        
        doc = self.spacyNlp(sentence)
        for token in doc:
            if token.head.i == actionToken.i and token.dep_ == SPACY_DEP_AGENT:
                agent = token
                break

        return agent

    def findThemeOfAction(self, sentence, actionToken):
        theme = None
        subject = self.parseTreeUtil.findSubjectOfToken(sentence, actionToken)
        senObject = self.parseTreeUtil.findObjectOfToken(sentence, actionToken)

        if actionToken.tag_ not in [SPACY_TAG_VB, SPACY_TAG_VBD, SPACY_TAG_VBG, SPACY_TAG_VBP, SPACY_TAG_VBZ]:
            theme = subject
        else:
            #theme = self.findToTokenAction(sentence, actionToken)
            theme = self.parseTreeUtil.findIndirectObjectOfToken(sentence, actionToken)

        return theme

    def findToTokenAction(self, sentence, actionToken):

        toToken = None
        doc = self.spacyNlp(sentence)
    	associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, actionToken)
    	for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]   
                if prep.text == PREP_TO:
                    toToken = token
                    break

        return toToken

    def isARelationshipExists(self, word1, word2):
          return self.conceptNet.checkRelationship(self.wordnetLemmatizer.lemmatize(word1), word2, CN_REL_IS_A)

    def isAnEvent(self, word1):
        return self.conceptNet.checkRelationship("", self.wordnetLemmatizer.lemmatize(word1), CN_HAS_SUBEVENT)

    def isAUnitOfTime(self, word1):
        return self.isARelationshipExists(token.text, "time_unit")

        
    






