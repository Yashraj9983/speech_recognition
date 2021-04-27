
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/indexjs')
def indexjs():
   return render_template('indexjs.html')

@app.route('/resultjs',methods = ['POST', 'GET'])
def resultjs():
   if request.method == 'POST':
      result = request.form
      return render_template("resultjs.html",result = result)


@app.route("/indexpy", methods=["GET", "POST"])
def indexpy():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('indexpy.html', transcript=transcript)      

if __name__ == '__main__':
   app.run(debug = True, threaded=True)