

from nltk.wsd import lesk

TYPE_PERSON_SYNSET = "person.n.01"
TYPE_ANIMAL_SYNET = "animal.n.01"
MAX_ITER_IS_A = 5
# return true if "word1" is-a "word2"
# Eg: returns true if word1 = cat, word2 = animal because cat is-a animal
def isARelationship(word1, word2, word1ContainingSentence=""):

	def isAUtil(word1Synset, word2Synset, numIter):
		if numIter ==  MAX_ITER_IS_A:
			return false
		hypernyms = word1Synset.hypernyms()
		if word2Synset in hypernyms:
			return True
	
		for hypernym in hypernyms:
			if isAUtil(hypernym, word2Synset, ++numIter):
				return True
	
		return False


	word1Synsets = wordnet.synsets(word1)
	word2Synset = wordnet.synset(word2)

	if word2Synset in word1Synsets:
		return True

	for syn in word1Synsets:
		if isAUtil(syn, word2Synset, 0):
			return True

	return False





