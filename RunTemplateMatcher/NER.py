class NER:

    def __init__(self, spacyNlp):
    	self.spacyNlp = spacyNlp
    	
	def printSpacyNamedEntities(sentence):
    	doc = self.spacyNlp(sentence)
    	print ("Named entities\n")
    	for ent in list(doc.ents):
    	    print(ent.text, ent.label_)