from SpacyConstants import *

class TemplateNamed:

    def __init__(self, spacyNlp, parseTreeUtil):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil

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
        print(sentence)
        print ("Who: ", whoWasNamed, "  name:", name)
        print('\n')

    
