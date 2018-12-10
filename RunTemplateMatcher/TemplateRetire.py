from SpacyConstants import *
class TemplateRetire:

    def __init__(self, spacyNlp, parseTreeUtil, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.semanticHelper = semanticHelper

    def parse(self, sentence):
    	if self.parseTreeUtil.getHeadOfSentence(sentence).text in ["retired", "retires", "retire"]:
           self.parseVerbForm(sentence)
        else:
           self.parseNounForm(sentence)

    def parseVerbForm(self, sentence):
        who = None
        fromWhat = None
        #why = None
        age = None
        doc = self.spacyNlp(sentence)

        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        who = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findSubjectOfToken(sentence, headToken))

        for prepId, prepToken in associatedPrepositionIds.items():
            if prepToken.text == PREP_OF:
                reason = self.parseTreeUtil.getSubTreeString(prepToken)
            if prepToken.text == PREP_FROM:
                fromWhat = self.parseTreeUtil.getSubTreeString(prepToken)           
            elif prepToken.text in [PREP_AT]:
                subTreeText = self.parseTreeUtil.getSubTreeString(prepToken)
                age = subTreeText
            
        print("who: ", who)
        print("from what: ", fromWhat)
        print("age: ", age)
        #print("reason: ")

    def parseNounForm(self, sentence):
    	who = None
        fromWhat = None
        #why = None
        age = None

        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        who = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))

        for prepId, prepToken in associatedPrepositionIds.items():
            if prepToken.text == PREP_OF:
                reason = self.parseTreeUtil.getSubTreeString(prepToken)
            if prepToken.text == PREP_FROM:
                fromWhat = self.parseTreeUtil.getSubTreeString(prepToken)           
            elif prepToken.text in [PREP_AT]:
                subTreeText = self.parseTreeUtil.getSubTreeString(prepToken)
                age = subTreeText

        print("who: ", who)
        print("from what: ", fromWhat)
        print("age: ", age)