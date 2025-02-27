from Word import Word
 
from flask import Flask, request, jsonify

from flask import send_from_directory

from flask_cors import CORS    

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Serve the HTML file
    return send_from_directory('static', 'viewFrame.html')


@app.route('/stop-lesson', methods=['POST'])
def stop_lesson():
    # logic to stop the lesson
    print("Got stop request")
    return jsonify({"status": "stopped", "message": "Lesson stopped"})


class Controller:
    def __init__(self):
        self.lessonRunning = False
        self.lessonLanguage = "NA"

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
            
        return 0

    def startLessonButtonPressed(self, language):
        self.lessonLanguage = language
        self.lessonRunning = True
        self.runLesson()

    def stopButtonPressed(self):
        self.lessonRunning = False
        print("Lesson stopped")
        return {"status": "stopped", "message": "Lesson stopped"}
        

    def getRandomWord(self): #temporary
        randomWord = Word("Hello","Bonjour","EnglishAudio/Hello.mp3","TranslatedAudio/Bonjour.mp3")
        return randomWord
    
    def getUserInput(self): #temporary
        return "Bonjour"

controller = Controller() 

if __name__ == '__main__':
    app.run(debug=True, port=5000)

