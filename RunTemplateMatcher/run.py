import spacy
from nltk.stem import WordNetLemmatizer

# Import other local files
from Constants import SpacyConstants
from ParseTreeUtil import ParseTreeUtil
from SemanticHelper import SemanticHelper
from Matcher import Matcher
from WSD import WSD


from TemplateNamed import TemplateNamed
from TemplateFine import TemplateFine
from TemplateDie import TemplateDie
from TemplatePay import TemplatePay
from TemplateTweets import TemplateTweets
from TemplateBan import TemplateBan
from TemplateShare import TemplateShare
from TemplateInjure import TemplateInjure
from TemplateRetire import TemplateRetire
from TemplateAccuse import TemplateAccuse
from TemplateApologize import TemplateApologize

print("Initializing spacy NLP model\n")
spacyNlp = spacy.load('en_core_web_lg')
wordnetLemmatizer = WordNetLemmatizer() 
#wsd = WSD()
#spacyNlp = None
parseTreeUtil = ParseTreeUtil(spacyNlp)
matcher = Matcher(spacyNlp, parseTreeUtil, wordnetLemmatizer)
semanticHelper = SemanticHelper(spacyNlp, parseTreeUtil, wordnetLemmatizer)

#Templates
templateBan = TemplateBan(spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper) # T1 4
templateFine = TemplateFine(spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper) # T3 4
templateShare = TemplateShare(spacyNlp, parseTreeUtil, wordnetLemmatizer) # T4 3 (+2)
templateInjure = TemplateInjure(spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper) # T5 5

templateDie = TemplateDie(spacyNlp, parseTreeUtil, semanticHelper) # T6 5
templatePay = TemplatePay(spacyNlp, parseTreeUtil, semanticHelper) # T7 4 (+1)
templateRetire = TemplateRetire(spacyNlp, parseTreeUtil, semanticHelper) # T8 3
templateAccuse = TemplateAccuse(spacyNlp, parseTreeUtil, semanticHelper) #T9 3
templateApologize = TemplateApologize(spacyNlp, parseTreeUtil, semanticHelper) #T10 3
templateNamed = TemplateNamed(spacyNlp, parseTreeUtil, semanticHelper) # T2 3


#templateTweets = TemplateTweets(spacyNlp, parseTreeUtil)
#injury - 5

def main():
    while(1):
       sentence = unicode(raw_input('Give a sentence\n'))
       processSentence(sentence)
       #templateNamed.parse(sentence)
       #templateFine.parse(sentence)
   

def processSentence(sentence):

    if (matcher.matchTemplateFine(sentence)):
    	print("Matched FINED template\n")
        templateFine.parse(sentence)

    if (matcher.matchTemplateBan(sentence)):
    	print("Matched BANNED template\n")
        templateBan.parse(sentence)

    if (matcher.matchTemplateNamed(sentence)):
    	print("Matched NAMED template\n")
        templateNamed.parse(sentence)
# --DF
    if (matcher.matchTemplateShare(sentence)):
    	print("Matched SHARED template\n")
        templateShare.parse(sentence)

    if (matcher.matchTemplateInjure(sentence)):
    	print("Matched INJURE template\n")
    	templateInjure.parse(sentence)

    if (matcher.matchTemplateDie(sentence)):
    	print("Matched DIE template\n")
        templateDie.parse(sentence)
    
    if (matcher.matchTemplatePay(sentence)):
    	print("Matched PAY template\n")
        templatePay.parse(sentence)

    if (matcher.matchTemplateRetire(sentence)):
    	print("Matched RETIRE template")
        templateRetire.parse(sentence)

    if (matcher.matchTemplateAccuse(sentence)):
    	print("Matched ACCUSED template")
    	templateAccuse.parse(sentence)

    if (matcher.matchTemplateApologize(sentence)):
    	print("Matched APOLOGISED template")
    	templateApologize.parse(sentence)


def test():
    with open('Data/inputTest') as data_file:
        sentences = data_file.readlines()

    for sentence in sentences:
        print(sentence)
        sentence = unicode(sentence)
        sentence = sentence.replace('\n', '')
        processSentence(sentence)
main()