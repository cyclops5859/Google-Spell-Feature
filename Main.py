#Made by Rehan Khan
#Modules to be installed pyttsx3 & SpeechRecognition

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("processing....") 
        text = r.recognize_google(audio,language='en-in')
    except Exception:               
        return "none"
    return text

speak('what is the word?')
spelling = takecom()
speak(spelling)
speak('is spelt')
for i in (spelling):
    speak(i)

