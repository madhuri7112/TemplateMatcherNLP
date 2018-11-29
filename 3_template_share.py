import spacy 

with open('share') as data_file:
        sentences = data_file.readlines()

nlp = spacy.load('en_core_web_sm')

def printTree(sentence):
	doc = nlp(unicode(sentence))
	 
	for token in doc:
	    print("{0}/{1} <--{2}-- {3}/{4}".format(
	        token.text, token.tag_, token.dep_, token.head.text, token.head.tag_))


SPACY_DEP_ROOT = "ROOT"
SPACY_DEP_NSUBJ = "nsubj"
SPACY_DEP_DOBJ = "dobj"
def getHeadOfSentence(sentence):

	doc = nlp(unicode(sentence))
	for token in doc:
		if token.dep_ == SPACY_DEP_ROOT:
			print (sentence, token.text)

def parse(sentence):
	doc = nlp(unicode(sentence))
	whoShared = None
	typeShared = None
	for token in doc:
		# if token.dep_ == SPACY_DEP_ROOT:
		# 	print (sentence, token.text)
		if token.dep_ == SPACY_DEP_NSUBJ:
			whoShared = token.text
		if token.dep_ == SPACY_DEP_DOBJ:
			typeShared = token.text
	print(sentence, typeShared, whoShared)



for sentence in sentences:
	sentence = sentence.replace('shares', 'shows')
	sentence = sentence.replace('share', 'show')
	#getHeadOfSentence(sentence)
	parse(sentence)

#printTree('Pitch invader shows selfie clicked by Cristiano Ronaldo for him')