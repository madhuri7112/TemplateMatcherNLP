from SpacyConstants import * 

class TemplateApologize:

    def __init__(self, spacyNlp, parseTreeUtil, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.semanticHelper = semanticHelper

    def parse(self, sentence):
        self.parseVerbForm(sentence)
        pass

    def parseVerbForm(self, sentence):
        
        whoApologized = None
        toWhom = None
        forWhat = None

        doc = self.spacyNlp(sentence)
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)

        whoApologized = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, headToken))
        toWhom = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findObjectOfToken(sentence, headToken))

        associatedPrepositionIds = self.parseTreeUtil.findPrepsAttachedToToken(sentence, headToken)

        for token in doc:
            if token.head.i in associatedPrepositionIds:
                prep = associatedPrepositionIds[token.head.i]
                if prep.text in [PREP_FOR, PREP_OF] :
                    forWhat = self.parseTreeUtil.getSubTreeString(token)
                elif prep.text == PREP_OVER:
                    forWhat = self.parseTreeUtil.getSubTreeString(token)

        print("whoApologized: ", whoApologized)
        print("toWhom: ", toWhom)
        print("forWhat: ", forWhat)
        print('\n')