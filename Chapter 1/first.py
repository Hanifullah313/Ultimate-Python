import pyjokes
joke = pyjokes.get_joke()
print(joke)

# pyttxs3 is used for text to speech conversion
import pyttsx3
engine = pyttsx3.init()
engine.say(joke)    
engine.runAndWait()