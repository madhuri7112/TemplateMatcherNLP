from SpacyConstants import * 
# Serena was fined 12 lakh $ for violations during US Open final loss
# Zlatan was handed fine for slapping opponent during match
# Afghan keeper was fined 100$ for playing in Pak

# Noun forms
# ICC handed coach 18 lakh fine over yellow ribbon
# Sachin was fined 18 lakh $ for ball tampering
# Man City coach was handed 18 lakh fine by FA over yellow ribbon

# Verb forms
# Serena was fined 12 lakh $ for violations during US Open final loss
# Afghan keeper was fined 100$ for playing in Pak

class TemplateFine:

    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer
        self.semanticHelper = semanticHelper

    def getAmountFined(self, sentence):
        doc = self.spacyNlp(sentence)
        amountFined = None
        for ent in list(doc.ents):
            if (ent.label_  == SPACY_NER_CARDINAL and amountFined == None) or ent.label_ == SPACY_NER_MONEY:
                amountFined = ent.text
                
        return amountFined
      
    def parse(self, sentence):
        if self.parseTreeUtil.getHeadOfSentence(sentence).text != "fined":
            #print (sentence)
            self.parseNounForm(sentence)        
        else:
            self.parseVerbForm(sentence)      
    
    def parseVerbForm(self, sentence):
        amount = None
        timePeriod = None
        reason = None
        whoGotFined = None
        whoImposedFined = None
        
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp((sentence))
    
        associatedPrepositionIds = {}

        whoImposedFined = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))
        whoGotFined = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findThemeOfAction(sentence, headToken))
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)

        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR] :
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_UNTIL:
                    timePeriod = self.parseTreeUtil.getSubTreeString(token)
        amount = self.getAmountFined(sentence)  

        print("who_got_fined: ", whoGotFined)
        print("who_fined: ", whoImposedFined)
        print("reason :", reason)
        print("amount :", amount)
        print('\n')
        
    def parseNounForm(self, sentence):
        #ASSUMPTION: Head verb is connected to "fine"
        amount = None
        reason = None
        whoGotFined = None
        whoImposedFined = None
        fineToken = None
        associatedPrepositionIds = {}
        doc = self.spacyNlp((sentence))
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
                
        for token in doc:       
            tokenLemma = self.wordnetLemmatizer.lemmatize(token.text)
            if tokenLemma == 'fine' or tokenLemma == 'fined':
                fineToken = token

        whoImposedFined = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))
        whoGotFined = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findThemeOfAction(sentence, headToken))
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)

            
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text == PREP_FOR :
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_FROM:
                    fromWhat = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    reason = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_TO:
                    who = self.parseTreeUtil.getSubTreeString(token)
            elif token.head.i == fineToken.i and token.tag_ in [SPACY_TAG_NN, SPACY_TAG_NNS, SPACY_TAG_NNP, SPACY_TAG_NNPS, SPACY_TAG_JJ,SPACY_TAG_JJR, SPACY_TAG_JJS]:
                timePeriod = self.parseTreeUtil.getSubTreeString(token)
        amount = self.getAmountFined(sentence)
        
        print("who_got_fined: ", whoGotFined)
        print("who_fined: ", whoImposedFined)
        print("reason :", reason)
        print("amount :", amount)
        print('\n')

