from SpacyConstants import * 

class TemplateAccuse:
    
    def __init__(self, spacyNlp, parseTreeUtil, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.semanticHelper = semanticHelper

    def parse(self, sentence):
    	self.parseVerbForm(sentence)
    	pass

    def parseVerbForm(self, sentence):
        
        whoAccused = None
        whoGotAccused = None
        forWhat = None

        doc = self.spacyNlp(sentence)
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)

        whoAccused = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))
        whoGotAccused = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findObjectOfToken(sentence, headToken))

        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)

        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR, PREP_OF] :
                    forWhat = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    forWhat = self.parseTreeUtil.getSubTreeString(token)

        print("whoAccused: ", whoAccused)
        print("whoGotAccused: ", whoGotAccused)
        print("forWhat: ", forWhat)
        print('\n')
                