#  Couldn't afford milk, now won medal: Asian Games bronze-winner
# There's nothing that I can't do: Vinesh on winning Asiad gold
# Bookable offence if India were to lose in Eng, Aus: Chappell
# Rahane promised me special knock for my 50th birthday: Coach
# Ronaldo is like port wine: Coach after forward's 4th WC goal

# Extra Examples
# Government Doesn't Need Extra Funds From RBI, Says Arun Jaitley
# Indira Gandhi's Bank Nationalisation Was A Fraud, Says PM Modi
#
# Virat said "I had enough of this"
#

# Negative examples
# La Liga: Santiago Solari, Sergio Ramos Feel Heat As Real Madrid Crash At Eibar
# 3rd Test: Adil Rashid England's Hero As Sri Lanka Collapse On Day 2
# Gold Prices Fall For Second Straight Day: 5 Things To Know


# Template: STATEMENT
# parametes: statement, who_said, to_whom, Subject

import * from util
import spacy
#import en_core_web_sm
#NER_PERSON_TAG = 
model='en_core_web_sm'
nlp = spacy.load(model)

def isSentenceStatement(sentence):
	pass

def parseStatementSentence(sentence):
	parseColonStatementSentence(sentence)

def parseColonStatementSentence(sentence):
	statement, info = sentence.split(':')
	infoDoc = nlp(info)
