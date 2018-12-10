from nltk.wsd import lesk
from SpacyConstants import * 

class Matcher:
    def __init__(self, spacyNlp, parseTreeUtil, wordnetLemmatizer):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil
        self.wordnetLemmatizer = wordnetLemmatizer

    def match(self, sentence):
        pass

    def matchTemplateFine(self, sentence):
        doc = self.spacyNlp(sentence)
        fineWordNoun = "fine"
        fineWordVerb = "fined"

        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in [fineWordNoun, fineWordVerb]:
                return True

        return False

    def matchTemplateBan(self, sentence):
        doc = self.spacyNlp(sentence)
        banWordNoun = "ban"
        banWordVerb = "banned"

        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in [banWordNoun, banWordVerb]:
                return True

    def matchTemplateNamed(self, sentence):
        doc = self.spacyNlp(sentence)
        namedWordVerb = "named"

        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in [namedWordVerb]:
                return True

    #def matchTemplateDie(self, sentence):
