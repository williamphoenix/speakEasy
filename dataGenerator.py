hi = dict(apple=[1,2,3],banana=[4,5,6],orange=[7,8,9])

class dataGenerator:

    precompiledDict = hi

    def __init__():
        print("classes dictionary is set to 'hi'")

    @staticmethod
    def getEnglishWord(key):
        return key
    
    @staticmethod
    def getTranslatedWord(key):
        return dataGenerator.precompiledDict[key][0]
    
    @staticmethod
    def getEnglishAudio(key):
        return dataGenerator.precompiledDict[key][1]
    
    @staticmethod
    def getTranslatedAudio(key):
        return dataGenerator.precompiledDict[key][2]
    

test = dataGenerator

print(test, "\n",
      hi, "\n",
      dataGenerator.getEnglishWord("apple"), "\n",
      dataGenerator.getTranslatedWord("banana"), "\n",
      dataGenerator.getEnglishAudio("apple"), "\n",
      dataGenerator.getTranslatedAudio("orange"), "\n",
      )