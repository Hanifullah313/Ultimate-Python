import speech_recognition as sr
import pyttsx3
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        speech("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in c.lower():
        speech("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open youtube" in c.lower():
        speech("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "stop" in c.lower() or "exit" in c.lower() or "quit" in c.lower():
        speech("Goodbye, Hanif!")
        exit()

if __name__ == "__main__":
    speech("Hello, I am your assistant. How can I help you?")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # sr microphone is used to capture audio from the microphone
            # it is the method of speech_recognition library
            try:
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=3)
                # listen method is used to capture the audio from the source
                # timeout is the maximum time to wait for a phrase to start
                # phrase_time_limit is the maximum time to wait for a phrase to end
                print("recognizing...")
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speech("Yes, how can I help you?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = r.listen(source , timeout=5 , phrase_time_limit=10)
                        command = r.recognize_google(audio)
                        processcommand(command)


            except Exception as e:
                print("Sorry, I could not understand the audio.")
                print("Error details:", e)
