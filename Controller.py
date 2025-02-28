from Word import Word
from Model import Model
from flask import Flask, request, jsonify

from flask import send_from_directory

from flask_cors import CORS 
import webbrowser
import threading   

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Serve the HTML file
    webbrowser.open("127.0.0.1:5000") #opens the browser with our window
    return send_from_directory('static', 'viewFrame.html')#points the flask server to the html file


@app.route('/stop-lesson', methods=['POST']) #gets the stop request from view and returns status that message was gotten
def stop_lesson():
    # logic to stop the lesson
    print("Got stop request")
    return jsonify({"status": "stopped", "message": "Lesson stopped"})


class Controller:
    def __init__(self):
        self.lessonRunning = False
        self.lessonLanguage = "NA"
        self.model = Model()
        self.startButtonPressed("French")

    def runLesson(self):
        print(f"Lesson running in {self.lessonLanguage}")
        if(self.lessonRunning == True):
            currentWord = self.model.getRandomWord() #change via model once implemented
            print("currentWord is:", currentWord.getEnglishWord())



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

    def startButtonPressed(self, language):
        self.lessonLanguage = language
        self.lessonRunning = True
        self.runLesson()

    def stopButtonPressed(self):
        self.lessonRunning = False
        print("Lesson stopped")
        return {"status": "stopped", "message": "Lesson stopped"}

controller = Controller() 

def openBrowser():
    # Wait for a moment to make sure the server is up
    import time
    time.sleep(1.5) #so that the browser doesn't open up too early
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Thread(target=openBrowser).start() #The Thread opens the browser, needs to be threaded so that doesnt block the flask server
    app.run(debug=True, port=5000) #Neccessary to run the flask server, force opens on port 5000 so that the web opener always goes to right port
