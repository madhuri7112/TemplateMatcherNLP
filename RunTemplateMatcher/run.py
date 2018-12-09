import spacy
from nltk.stem import WordNetLemmatizer

# Import other local files
from Constants import SpacyConstants
from ParseTreeUtil import ParseTreeUtil
from WSD import WSD

from TemplateNamed import TemplateNamed
from TemplateFine import TemplateFine
from TemplateDie import TemplateDie
from TemplatePay import TemplatePay
from TemplateTweets import TemplateTweets
from TemplateBan import TemplateBan
from TemplateShare import TemplateShare



def main():
    print("Initializing spacy NLP model\n")
    spacyNlp = spacy.load('en_core_web_sm')
    wordnetLemmatizer = WordNetLemmatizer() 
    wsd = WSD()
    #spacyNlp = None
    parseTreeUtil = ParseTreeUtil(spacyNlp)

    #Templates
    templateNamed = TemplateNamed(spacyNlp, parseTreeUtil)
    templateFine = TemplateFine(spacyNlp, parseTreeUtil, wordnetLemmatizer)
    templateDie = TemplateDie(spacyNlp, parseTreeUtil)
    templatePay = TemplatePay(spacyNlp, parseTreeUtil)
    templateTweets = TemplateTweets(spacyNlp, parseTreeUtil)
    templateBan = TemplateBan(spacyNlp, parseTreeUtil, wordnetLemmatizer)
    templateShare = TemplateShare(spacyNlp, parseTreeUtil, wordnetLemmatizer)

    while(1):
       sentence = unicode(raw_input('Give a sentence\n'))
       #templateNamed.parse(sentence)
       #templateFine.parse(sentence)
       templateFine.parse(sentence)

       #print(sentence)

main()