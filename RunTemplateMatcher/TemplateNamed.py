from SpacyConstants import *

class TemplateNamed:

    def __init__(self, spacyNlp, parseTreeUtil, semanticHelper):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.semanticHelper = semanticHelper

    def parse(self, sentence):
        doc = self.spacyNlp(sentence)
        whoWasNamed = None
        name = None
        headToken = self.parseTreeUtil.getHeadOfSentence(sentence)
        namedToken = None
        for token in doc:
            if token.text == "named":
                namedToken = token 
        for token in doc:
            if token.dep_ in [SPACY_DEP_NSUBJ, SPACY_DEP_NSUBJ_PASS]:
                whoWasNamed = self.parseTreeUtil.getSubTreeString(token)
            elif token.dep_ in SPACY_OBJECTS:
                name = self.parseTreeUtil.getSubTreeString(token)

        whoNamed = self.parseTreeUtil.getSubTreeString(self.semanticHelper.findAgentOfAction(sentence, namedToken))
        print(sentence)
        print ("who was named: ", whoWasNamed)
        print("name:", name)
        print("who named: " ,whoNamed)
        print('\n')

    
