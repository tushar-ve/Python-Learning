import speech_recognition as sr
import pyttsx3

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
  
     print("Listening....")
     r.pause_threshold = 1
     audio = r.listen(source)
     print("Listening....")
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
    return "None"

    return query