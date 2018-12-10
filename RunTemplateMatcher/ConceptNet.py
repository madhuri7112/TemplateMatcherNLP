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
    	
    	print("....Checking relationship: ", relationship, " between ", word1, " ", word2, " with conceptNet.io.......\n")
        #querystring = {"start": self.getUrlOfPhrase(word1), "end": self.getUrlOfPhrase(word2), "rel": relationship}
        querystring = {}
        if word1 != "":
            querystring["start"] = self.getUrlOfPhrase(word1)
        if word2 != "":
            querystring["end"] = self.getUrlOfPhrase(word2)
        if relationship != "":
            querystring["rel"] = relationship
        
        print("Query: ",querystring)
        response = requests.request("GET", self.queryUrl, params=querystring)
        resultJson = json.loads(response.text)
        print (len(resultJson["edges"]))
        #print(resultJson["edges"])
        return len(resultJson["edges"]) > 0
        	

# cn = ConceptNet()
# cn.checkRelationship("month", "time", "/r/IsA")





