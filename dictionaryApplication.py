import json
import difflib
from difflib import get_close_matches

file = open("data.json")
dictionaryData = json.load(file)

# Returning the defintions of word
def getTranslation(word):
	word = word .lower()
	if word in dictionaryData:
	   return dictionaryData[word];
	elif word.title() in dictionaryData: # in case of Nouns 
		return dictionaryData[word.title()];
	elif word.upper() in dictionaryData: # in case of acronyms
		return dictionaryData[word.upper()];
	#get_close_matches used to get closest match to the misspelt word by the user
	elif len(get_close_matches(word, dictionaryData.keys())) >0:
		bestMatch = get_close_matches(word, dictionaryData.keys())[0]
		response = raw_input("Did you mean %s? Enter Y if yes or N if No" % bestMatch)
		response = response.upper();
		if response == "Y":
			return dictionaryData[bestMatch]
		elif response == "N":
			return "The word doesn't exist. Please re-check it"
		else:
			return "Cannot understand your request"
	else:
		return "The word doesn't exist. Please re-check it"	

word = raw_input("Please enter the word ")
searchResult = getTranslation(word)

if(type(searchResult) == list):
	for result in searchResult:
		print(str(searchResult.index(result)+1)+ ": "+result);
else:
	print(searchResult)