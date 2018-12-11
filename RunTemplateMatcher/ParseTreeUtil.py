from SpacyConstants import * 
class ParseTreeUtil:

    def __init__(self, spacyNlp):
        self.spacyNlp = spacyNlp

    def getSubTreeString(self, token):
        
        if not token:
            return ""
            
        return ' '.join([str(token1.text) for token1 in list(token.subtree)])

    def getHeadOfSentence(self, sentence):
    
        doc = self.spacyNlp(unicode(sentence))
        head = None
        for token in doc:
            if token.dep_ == SPACY_DEP_ROOT:
                #print ("head",sentence, token.text)
                head = token
                
        return head  
    
    def printTree(self, sentence):
        doc = self.spacyNlp(unicode(sentence))
     
        for token in doc:
            print("{5}: {0}/{1} <--{2}-- {3}/{4} > {6};  type {7}".format(
               token.text, token.tag_, token.dep_, token.head.text, token.head.tag_,token.i,token.head.i, token.ent_id_))
            
            print(list(token.subtree))
            print ('**********')

    def findSubjectOfToken(self, sentence, targetToken):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if token.head.i == targetToken.i and  token.dep_ in [SPACY_DEP_NSUBJ_PASS, SPACY_DEP_NSUBJ]:
                return token
        
        return None
        
    def findPrepsAttachedToToken(self, sentence, targetToken):
        doc = self.spacyNlp(sentence)
        associatedPrepositionIds = {}
        for token in doc:
            if token.head.i == targetToken.i and token.tag_ == SPACY_TAG_PREP:
                associatedPrepositionIds[token.i] = token
        
        return associatedPrepositionIds

    def findObjectOfToken(self, sentence, targetToken):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if token.head.i == targetToken.i and  token.dep_ in [SPACY_DEP_DOBJ]:
                return token
        
        return None

    def findRootWordForPP(self, sentence, prepToken):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if token.head.i == prepToken.i:
                return token

    def findIndirectObjectOfToken(self, sentence, targetToken):
        doc = self.spacyNlp(sentence)
        for token in doc:
            if token.head.i == targetToken.i and  token.dep_ in [SPACY_DEP_IND_OBJ_1, SPACY_DEP_IND_OBJ_2]:
                return token
        
        return None