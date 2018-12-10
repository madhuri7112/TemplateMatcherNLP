import SpacyConstants

class TemplateDie:

    def __init__(self, spacyNlp, parseTreeUtil):
        self.spacyNlp = spacyNlp
        self.parseTreeUtil = parseTreeUtil

    def parse(self, sentence):
        rootWord = self.parseTreeUtil.getHeadOfSentence(sentence)
        whoDied = None
        whereDied = None
        whenDied = None
        age = None
        reason = None
        
        whoDied = self.parseTreeUtil.getSubTreeString(self.parseTreeUtil.findSubjectOfToken(sentence, rootWord))
        preps = self.parseTreeUtil.findPrepsAttachedToToken(sentence, rootWord)
        
        for prepId, prepToken in preps.items():
            if prepToken.text == SpacyConstants.PREP_OF:
                reason = self.parseTreeUtil.getSubTreeString(prepToken)
            
            elif prepToken.text in [SpacyConstants.PREP_AT, SpacyConstants.PREP_NEAR]:
                subTreeText = self.parseTreeUtil.getSubTreeString(prepToken)
                if 'age'  not in subTreeText:
                    whereDied = subTreeText
                else:
                    age = subTreeText
            elif prepToken.text == SpacyConstants.PREP_ON:
                whenDied = self.parseTreeUtil.getSubTreeString(prepToken)
            elif prepToken.text in [SpacyConstants.PREP_IN]:
                pass
        print(sentence)            
        print ("Who: " ,whoDied, "where: ", whereDied, "whenDied: ", whenDied, "age: ", age, "reason: ", reason)
        print("\n")

    
