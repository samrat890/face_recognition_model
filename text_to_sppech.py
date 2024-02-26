import pyttsx3

# engine = pyttsx3.init()
# a="good morning"
# engine.say(a)
# engine.say("thank you")
# engine.runAndWait()
# way 2
from gtts import gTTS
import os

mytext = "omdayal group of institutions"
language="en"
myobj = gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")