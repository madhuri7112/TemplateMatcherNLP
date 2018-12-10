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

print("Initializing spacy NLP model\n")
spacyNlp = spacy.load('en_core_web_lg')
wordnetLemmatizer = WordNetLemmatizer() 
#wsd = WSD()
#spacyNlp = None
parseTreeUtil = ParseTreeUtil(spacyNlp)
matcher = Matcher(spacyNlp, parseTreeUtil, wordnetLemmatizer)
semanticHelper = SemanticHelper(spacyNlp, parseTreeUtil, wordnetLemmatizer)

#Templates
templateBan = TemplateBan(spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper) # 4
templateNamed = TemplateNamed(spacyNlp, parseTreeUtil, semanticHelper) # 3
templateFine = TemplateFine(spacyNlp, parseTreeUtil, wordnetLemmatizer, semanticHelper) # 4

templateShare = TemplateShare(spacyNlp, parseTreeUtil, wordnetLemmatizer)
templateDie = TemplateDie(spacyNlp, parseTreeUtil)
templatePay = TemplatePay(spacyNlp, parseTreeUtil)
templateTweets = TemplateTweets(spacyNlp, parseTreeUtil)


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

def test():
    with open('Data/ban') as data_file:
        sentences = data_file.readlines()

    for sentence in sentences:
        print(sentence)
        sentence = unicode(sentence)
        sentence = sentence.replace('\n', '')
        processSentence(sentence)
main()