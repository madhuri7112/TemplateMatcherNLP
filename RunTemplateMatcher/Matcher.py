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

    def matchTemplateShare(self, sentence):
        doc = self.spacyNlp(sentence)
        
        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["shares", "shared", "share"]:
                return True
    #death - not done
    def matchTemplateDie(self, sentence):
        doc = self.spacyNlp(sentence)

        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["die", "died", "dies", "dead", "dy"]:
                return True

        return False

    def matchTemplateInjure(self, sentence):
        doc = self.spacyNlp(sentence)
        #injure
        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["injured", "injury"]:
                return True
    # payment - not done
    def matchTemplatePay(self, sentence):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["pay", "paid"]:
                return True

    #retirement - not done
    def matchTemplateRetire(self, sentence):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["retire", "retired", "retires", "retirement"]:
                return True

    #Accusation - Not done
    def matchTemplateAccuse(self, sentence):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["accuse", "accuses", "accused"]:
                return True
    
    # Apology - Not done
    def matchTemplateApologize(self, sentence):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if self.wordnetLemmatizer.lemmatize(token.text) in ["apologize", "apologizes", "apologized", "apologises", "apologise"]:
                return True