from Word import Word
from Model import Model
from flask import Flask, request, jsonify, abort

from flask import send_from_directory

from flask_cors import CORS 
import webbrowser
import threading
import ffmpeg
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

recordings_path = os.path.join(os.path.dirname(__file__), 'recordings')

@app.route('/')
def index():
    return send_from_directory('static', 'viewFrame.html')#points the flask server to the html file


class Controller:
    def __init__(self):
        self.lessonRunning = False
        self.lessonLanguage = "NA"
        self.model = Model()
        self.currentWord = self.model.getRandomWord()

    def getCurrentWord(self):
        return self.currentWord

    def runLesson(self):
        print(f"Lesson running in {self.lessonLanguage}")
        if(self.lessonRunning == True):
            self.currentWord = self.model.getRandomWord()
            print("currentWord is:", self.currentWord.getEnglishWord())

            #sends randomly generated word to the view
        

            #recieves user responce from view

            #sends user responce to the model

            #gets processed word as text from Model

            #check for stop command

            if("tempString".lower() in self.currentWord.getTranslatedWord().lower()):#check if correct
                print("got here")
                #send correct signal to view
                return 0
            else:
                #send incorrect signal to view
                #send correct translation to view
                return 0
            
        return 0

    def startButtonPressed(self):
        self.lessonRunning = True
        self.runLesson()

    def stopButtonPressed(self):
        self.lessonRunning = False
        print("Lesson stopped")
        self.currentWord = self.model.getRandomWord()
        return {"status": "stopped", "message": "Lesson stopped"}
        

controller = Controller() 

@app.route('/start-lesson', methods=['POST']) #gets the stop request from view and returns status that message was gotten
def startLesson():
    dropdownData = request.get_json()
    controller.lessonLanguage = dropdownData.get("language", "Unknown")
    # logic to stop the lesson
    print("Got start request")
    controller.startButtonPressed()
    return jsonify({"status": "started", "message": "Lesson started"})

@app.route('/get_string')
def get_string():
    print("We're in get_string")
    my_string = controller.getCurrentWord().getEnglishWord()
    print(my_string)
    return jsonify({'data': my_string})


@app.route('/stop-lesson', methods=['POST']) #gets the stop request from view and returns status that message was gotten
def stopLesson():
    # logic to stop the lesson
    print("Got stop request")
    controller.stopButtonPressed()
    return jsonify({"status": "stopped", "message": "Lesson stopped"})

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'audio_file' not in request.files:
        return abort(400, 'No audio file part')
    
    audio_file = request.files['audio_file']
    if audio_file.filename == '':
        return abort(400, 'No selected file')
    
    save_path = os.path.join(recordings_path, audio_file.filename)
    audio_file.save(save_path)

    return jsonify({'message': 'File saved successfully', 'path': save_path})

def openBrowser():
    # Wait for a moment to make sure the server is up
    import time
    time.sleep(1.5) #so that the browser doesn't open up too early
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Thread(target=openBrowser).start() #The Thread opens the browser, needs to be threaded so that doesnt block the flask server
    app.run(debug=True, port=5000) #Neccessary to run the flask server, force opens on port 5000 so that the web opener always goes to right port
