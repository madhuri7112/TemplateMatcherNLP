import requests
import json

from ConceptNetConstants import * 

class ConceptNet:
    def __init__(self):
    	self.queryUrl = "http://api.conceptnet.io/query"

    def getUrlOfPhrase(self, phrase):
    	phrase = phrase.strip()
    	phrase = phrase.replace(' ', '_')
    	return "/c/en/"+phrase
    # checks. word1 ---relationship---> word2 is true/false
    def checkRelationship(self, word1, word2, relationship):
    	
    	print("....Checking relationship between ", word1, " ", word2, " with conceptNet.io.......\n")
        querystring = {"start": self.getUrlOfPhrase(word1), "end": self.getUrlOfPhrase(word2), "rel": relationship}
        
        response = requests.request("GET", self.queryUrl, params=querystring)
        resultJson = json.loads(response.text)
        #print(resultJson["edges"])
        return len(resultJson["edges"]) > 0
        	

# cn = ConceptNet()
# cn.checkRelationship("month", "time", "/r/IsA")





