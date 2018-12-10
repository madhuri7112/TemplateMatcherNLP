from SpacyConstants import * 
# add whoGotPaid
class TemplatePay:
    def __init__(self, spacyNlp, parseTreeUtil, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.semanticHelper = semanticHelper

    def getAmountPaid(self, sentence):
        doc = self.spacyNlp(sentence)
        amountFined = None
        for ent in list(doc.ents):
            if (ent.label_  == SPACY_NER_CARDINAL and amountFined == None) or ent.label_ == SPACY_NER_MONEY:
                amountFined = ent.text
                
        return amountFined

    def parse(self, sentence):
        self.parseVerbForm(sentence)

    def parseVerbForm(self, sentence):
        amount = None
        timePeriod = None
        reason = None
        who = None
        fromWhat = None
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp(sentence)
        whatPaid = None
        associatedPrepositionIds = {}
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        #Find associated Prep Ids and subject
        # for token in doc:
        #     #print ("ref", token.text, token.head.i, token.head.head.i)
        #     if token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]):
        #         who = self.parseTreeUtil.getSubTreeString(token)
        who = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))
        whatPaid = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findObjectOfToken(sentence, headToken))
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR, PREP_AS] :
                    reason = self.parseTreeUtil.getSubTreeString(token)
            # if token.head.i == headToken.i and token.dep_ in SPACY_OBJECTS:
            #     whatPaid = self.parseTreeUtil.getSubTreeString(token)
        amount = self.getAmountPaid(sentence)  
        if (whatPaid == None or whatPaid == "")and amount != None:
            whatPaid = "money"
        print(sentence)
        print(" who: ", who,
             " reason :", reason,
             " amount :", amount,
              "what: ", whatPaid,'\n')