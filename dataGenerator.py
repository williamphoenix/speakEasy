import pandas as pd

        
class dataGenerator:
    
    def __init__(self):
        self.FrenchDict = self.compileDict("EnglishToFrenchNouns.csv")
        self.SpanishDict = self.compileDict("EnglishToSpanishNouns.csv")
        self.EnglishDict = self.compileDict("EnglishToEnglishNouns.csv")

    @staticmethod
    def compileDict(path):
        current = pd.read_csv(path)
        currentDict = dict()
        for i in range(len(current)):
            currentDict.setdefault(current["EnglishWord"][i],
                            [current["TranslatedWord"][i],
                            current["Prompt"][i],
                            current["Response"][i]])
        return currentDict

    def getDict(self, lang):
        if(lang == "French"):
            return self.FrenchDict
        elif(lang == "Spanish"):
            return self.SpanishDict
        elif(lang == "English"):
            return self.EnglishDict
        else:
            raise("did not find language to access")
    

    def getEnglishWord(self, key):
        return key
    

    def getTranslatedWord(self, key):
        return dataGenerator.precompiledDict[key][0]
    

    def getEnglishAudio(self, key):
        return dataGenerator.precompiledDict[key][1]
    

    def getTranslatedAudio(self, key):
        return dataGenerator.precompiledDict[key][2]
    

#print("This is the test csv dataframe: \n", test, "\n",
#      "This is the dictionary test: \n", testDict, "\n",
#      dataGenerator.getEnglishWord("Hello"), "\n",
#      dataGenerator.getTranslatedWord("Apple"), "\n",
#      dataGenerator.getEnglishAudio("House"), "\n",
#      dataGenerator.getTranslatedAudio("Hello"), "\n",
#      )