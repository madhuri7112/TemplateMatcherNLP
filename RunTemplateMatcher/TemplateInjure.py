from  SpacyConstants import * 
# Sachin suffers a hand injury on Wednesday after bowling
# Sachin suffers a hand injury on Wednesday
# Sachin was injured during world cup on Wednesday
# Sachin injured his leg during world cup on Wednesday
class TemplateInjure:

    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer
        self.semanticHelper = semanticHelper

    def parse(self, sentence):
        if self.parseTreeUtil.getHeadOfSentence(sentence).text != "injured":
            #print (sentence)
            self.parseNounForm(sentence)        
        else:
            self.parseVerbForm(sentence)

    def parseVerbForm(self, sentence):
        rootWord = self.parseTreeUtil.getHeadOfSentence(sentence)
        whoGotInjured = None
        whereInjured = None
        whenInjured = None
        howInjured = None
        whatGotInjured = None
        
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        doc = self.spacyNlp(sentence)
   
        #Find associated Prep Ids and subject
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        
        whoGotInjured = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findSubjectOfToken(sentence, headToken))
        whatGotInjured = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findObjectOfToken(sentence, headToken))
       
                
        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR, PREP_AFTER, PREP_OVER, PREP_BY] :
                    howInjured = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text in [PREP_AT, PREP_DURING]:
                    whereInjured = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_ON:
                    whenInjured = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text in [PREP_IN]:
                    rootWordForPP = self.parseTreeUtil.findRootWordForPP(sentence, prep)
                    if self.semanticHelper.isAnEvent(rootWordForPP.text):
                        howInjured = self.parseTreeUtil.getSubTreeString(prep)
                    else:
                        whereInjured = self.parseTreeUtil.getSubTreeString(prep)
                    
        
        print(" who: ", whoGotInjured,
             " whereInjured : ", whereInjured,
             " whenInjured : ", whenInjured,"howInjured: " , howInjured, "whatGotInjured: ", whatGotInjured)
        print('\n')

    def parseNounForm(self, sentence):
      

        whoGotInjured = None
        whereInjured = None
        whenInjured = None
        howInjured = None
        whatGotInjured = None 

        doc = self.spacyNlp(sentence)
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        
        #print(headToken.text)
        #print(self.parseTreeUtil.printTree())

        whoGotInjured = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findSubjectOfToken(sentence, headToken)) 
        whatGotInjured = self.extractWhatGotInjured(sentence)
        for token in doc:       
            tokenLemma = self.wordnetLemmatizer.lemmatize(token.text)
            if tokenLemma == 'injure' or tokenLemma == 'injury':
                injuryToken = token
           
        # Fetching preps connected to Ban tag
        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)
        #print(associatedPrepositionIds)
        #self.parseTreeUtil.printTree(sentence)

        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR, PREP_AFTER, PREP_OVER] :
                    howInjured = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text in [PREP_AT, PREP_DURING]:
                    whereInjured = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_ON:
                    whenInjured = self.parseTreeUtil.getSubTreeString(token)
        
        print(sentence)
        print(" who: ", whoGotInjured,
             " whereInjured : ", whereInjured,
             " whenInjured : ", whenInjured,"howInjured: " , howInjured, "whatGotInjured: ", whatGotInjured)
        print('\n')

    def extractWhatGotInjured(self, sentence):
        doc = self.spacyNlp(sentence)
        injuryToken = None
        for token in doc:
            tokenLemma = self.wordnetLemmatizer.lemmatize(token.text)
            if tokenLemma == 'injure' or tokenLemma == 'injury':
                injuryToken = token

        if not injuryToken:
            return None

        for token in doc:
            if token.head.i == injuryToken.i and token.dep_ == SPACY_DEP_COMPOUND:
                return token.text
#retired