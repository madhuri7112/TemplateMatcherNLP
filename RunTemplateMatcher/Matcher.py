from nltk.wsd import lesk

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
        	if token in [fineWordNoun, fineWordVerb]:
        		return parseTreeUtil

        return False