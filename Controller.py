from Word import Word

class Controller:
    def __init__(self):
        self.lessonRunning = False
        self.lessonLanguage = "NA"
        self.startLessonButtonPressed("French")  #temp

    def runLesson(self):
        print(f"Lesson running in {self.lessonLanguage}")
        if(self.lessonRunning == True):
            currentWord = self.getRandomWord()#change via model once implemented



            #sends randomly generated word to the view

            #recieves user responce from view

            userResponse = self.getUserInput()#temp

            #sends user responce to the model

            #gets processed word as text from Model

            #check for stop command

            if(userResponse == currentWord.getTranslatedWord()):#check if correct
                print("got here")
                #send correct signal to view
                return 0
            else:
                #send incorrect signal to view
                #send correct translation to view
                return 0
            
            runLesson(self)
        return 0

    def startLessonButtonPressed(self, language):
        self.lessonLanguage = language
        self.lessonRunning = True
        self.runLesson()

    def stopButtonPressed(self):
        self.lessonRunning = False
        print("Lesson stopped")

    def getRandomWord(self): #temporary
        randomWord = Word("Hello","Bonjour","EnglishAudio/Hello.mp3","TranslatedAudio/Bonjour.mp3")
        return randomWord
    
    def getUserInput(self): #temporary
        return "Bonjour"


controller = Controller() 
controller.stopButtonPressed()  