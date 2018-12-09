from SpacyConstants import * 

class TemplatePay:
    def __init__(self, spacyNlp, parseTreeUtil):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil

    def getAmountPaid(self, sentence):
        doc = self.spacyNlp(sentence)
        amountFined = None
        for ent in list(doc.ents):
            if (ent.label_  == SPACY_NER_CARDINAL and amountFined == None) or ent.label_ == SPACY_NER_MONEY:
                amountFined = ent.text
                
        return amountFined

    def parse(self, sentence):
        amount = None
        timePeriod = None
        reason = None
        who = None
        fromWhat = None
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp(sentence)
        whatPaid = None
        associatedPrepositionIds = {}
        
        #Find associated Prep Ids and subject
        for token in doc:
            #print ("ref", token.text, token.head.i, token.head.head.i)
            if (token.head.i == headToken.i) and token.tag_ == SPACY_TAG_PREP:
                associatedPrepositionIds[token.i] = token
            elif token.head.i == headToken.i and (token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]):
                who = self.parseTreeUtil.getSubTreeString(token)
        print (associatedPrepositionIds)      
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR, PREP_AS] :
                    reason = self.parseTreeUtil.getSubTreeString(token)
            if token.head.i == headToken.i and token.dep_ in SPACY_OBJECTS:
                whatPaid = self.parseTreeUtil.getSubTreeString(token)
        amount = self.getAmountPaid(sentence)  
        if whatPaid == None and amount != None:
            whatPaid = "money"
        print(sentence)
        print(" who: ", who,
             " reason :", reason,
             " amount :", amount,
              "what: ", whatPaid,'\n')