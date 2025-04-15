from Word import Word
from Model import Model
from flask import Flask, request, jsonify, abort, Response

from flask import send_from_directory

from flask_cors import CORS 
import webbrowser
import threading
import ffmpeg
import os
import time

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
        self.awaitingResponse = False
        self.lessonLanguage = "NA"
        self.model = Model()

    def getCurrentWord(self):
        return self.currentWord

    def runLesson(self):
        print(f"Lesson running in {self.lessonLanguage}")
        if(self.lessonRunning == True):
            while self.lessonRunning:
                if not self.awaitingResponse:
                    self.currentWord = self.model.getRandomWord(self.lessonLanguage)
                    englishWord = self.currentWord.getEnglishWord()
                    print("New word:", englishWord)
                    yield f"data: {englishWord}\n\n"
                    self.awaitingResponse = True
                
                time.sleep(0.1)


    def processUserAudio(self, audio_path):
        score = self.model.checkTranslation(audio_path, self.currentWord.getEnglishWord())
        print("The score is", score)

        if score > 0:
            feedback = "Correct!"
        else:
            feedback = f"Incorrect! The correct word was '{self.currentWord.getEnglishWord()}'."

        print("Feedback:", feedback)

        yield f"{feedback}\n"

        self.awaitingResponse = False



    def startButtonPressed(self):
        self.lessonRunning = True
        self.runLesson()

    def stopButtonPressed(self):
        self.lessonRunning = False
        print("Lesson stopped")
        self.currentWord = self.model.getRandomWord(self.lessonLanguage)
        return {"status": "stopped", "message": "Lesson stopped"}
    
    @staticmethod
    def convertAudio(input_file, output_file):
        try:
            (
                ffmpeg
                .input(input_file)
                .output(output_file, format = "mp3", audio_bitrate='192k')
                .run(overwrite_output = True)
            )
            print(f"Conversion successful: {output_file}")
        except ffmpeg.Error as e:
            print("Error:", e.stderr.decode())
        

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
    
    original_path = os.path.join(recordings_path, audio_file.filename)
    audio_file.save(original_path)

    mp3_filename = os.path.splitext(audio_file.filename)[0] + ".mp3"
    mp3_path = os.path.join(recordings_path, mp3_filename)

    controller.convertAudio(original_path, mp3_path)

    print(f"Saved file: {original_path}, Converted to MP3: {mp3_path}")

    if os.path.exists(original_path):
        os.remove(original_path)

    def generate_feedback():
        for feedback in controller.processUserAudio(mp3_path):
            yield feedback

    return Response(controller.processUserAudio(mp3_path), mimetype="text/event-stream")

@app.route('/wordStream')
def wordStream():
    def generate():
        while controller.lessonRunning:
            for event in controller.runLesson():
                yield event
    return Response(generate(), mimetype="text/event-stream")

@app.route('/uploadAudio')
def uploadAudio():
    def generateAudio():
        currentWord = controller.getCurrentWord()
        print("English audio path is:",currentWord.getEnglishAudio())
        with open(currentWord.getEnglishAudio(), 'rb') as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)
    return Response(generateAudio(), mimetype="audio/mpeg")
    
def openBrowser():
    # Wait for a moment to make sure the server is up
    import time
    time.sleep(1.5) #so that the browser doesn't open up too early
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Thread(target=openBrowser).start() #The Thread opens the browser, needs to be threaded so that doesnt block the flask server
    app.run(debug=True, port=5000, use_reloader=False) #Neccessary to run the flask server, force opens on port 5000 so that the web opener always goes to right port
